"""
An FTP client class and some helper functions.
"""

import os
import sys

# Import SOCKS module if it exists, else standard socket module socket
try:
    import SOCKS; socket = SOCKS; del SOCKS # import SOCKS as socket
    from socket import getfqdn; socket.getfqdn = getfqdn; del getfqdn
except ImportError:
    import socket
from socket import _GLOBAL_DEFAULT_TIMEOUT

__all__ = ["FTP","Netrc"]

# Magic number from <socket.h>
MSG_OOB = 0x1                           # Process data out of band


# The standard FTP server control port
FTP_PORT = 21


# Exception raised when an error or invalid response is received
class Error(Exception): pass
class error_reply(Error): pass          # unexpected [123]xx reply
class error_temp(Error): pass           # 4xx errors
class error_perm(Error): pass           # 5xx errors
class error_proto(Error): pass          # response does not begin with [1-5]


# All exceptions (hopefully) that may be raised here and that aren't
# (always) programming errors on our side
all_errors = (Error, IOError, EOFError)


# Line terminators (we always output CRLF, but accept any of CRLF, CR, LF)
CRLF = '\r\n'

# The class itself
class FTP:

    '''An FTP client class.

    To create a connection, call the class using these arguments:
            host, user, passwd, acct, timeout

    The first four arguments are all strings, and have default value ''.
    timeout must be numeric and defaults to None if not passed,
    meaning that no timeout will be set on any ftp socket(s)
    If a timeout is passed, then this is now the default timeout for all ftp
    socket operations for this instance.

    Then use self.connect() with optional host and port argument.

    To download a file, use ftp.retrlines('RETR ' + filename),
    or ftp.retrbinary() with slightly different arguments.
    To upload a file, use ftp.storlines() or ftp.storbinary(),
    which have an open file as argument (see their definitions
    below for details).
    The download/upload functions first issue appropriate TYPE
    and PORT or PASV commands.
	'''

    debugging = 0
    host = ''
    port = FTP_PORT
    sock = None
    file = None
    welcome = None
    passiveserver = 1

    # Initialization method (called by class instantiation).
    # Initialize host to localhost, port to standard ftp port
    # Optional arguments are host (for connect()),
    # and user, passwd, acct (for login())
    def __init__(self, host='', user='', passwd='', acct='',
                 timeout=_GLOBAL_DEFAULT_TIMEOUT):
        self.timeout = timeout
        if host:
            self.connect(host)
            if user:
                self.login(user, passwd, acct)

    def connect(self, host='', port=0, timeout=-999):
        '''Connect to host.  Arguments are:
         - host: hostname to connect to (string, default previous host)
         - port: port to connect to (integer, default previous port)
        '''
        if host != '':
            self.host = host
        if port > 0:
            self.port = port
        if timeout != -999:
            self.timeout = timeout
        self.sock = socket.create_connection((self.host, self.port), self.timeout)
        self.af = self.sock.family
        self.file = self.sock.makefile('rb')
        self.welcome = self.getresp()
        return self.welcome

    def getwelcome(self):
        '''Get the welcome message from the server.
        (this is read and squirreled away by connect())'''
        if self.debugging:
            print '*welcome*', self.sanitize(self.welcome)
        return self.welcome

    def set_debuglevel(self, level):
        '''Set the debugging level.
        The required argument level means:
        0: no debugging output (default)
        1: print commands and responses but not body text etc.
        2: also print raw lines read and sent before stripping CR/LF'''
        self.debugging = level
    debug = set_debuglevel
	
	def set_pasv(self, val):
        '''Use passive or active mode for data transfers.
        With a false argument, use the normal PORT mode,
        With a true argument, use the PASV command.'''
        self.passiveserver = val

    # Internal: "sanitize" a string for printing
    def sanitize(self, s):
        if s[:5] == 'pass ' or s[:5] == 'PASS ':
            i = len(s)
            while i > 5 and s[i-1] in '\r\n':
                i = i-1
            s = s[:5] + '*'*(i-5) + s[i:]
        return repr(s)

    # Internal: send one line to the server, appending CRLF
    def putline(self, line):
        line = line + CRLF
        if self.debugging > 1: print '*put*', self.sanitize(line)
        self.sock.sendall(line)

    # Internal: send one command to the server (through putline())
    def putcmd(self, line):
        if self.debugging: print '*cmd*', self.sanitize(line)
        self.putline(line)

    # Internal: return one line from the server, stripping CRLF.
    # Raise EOFError if the connection is closed
    def getline(self):
        line = self.file.readline()
        if self.debugging > 1:
            print '*get*', self.sanitize(line)
        if not line: raise EOFError
        if line[-2:] == CRLF: line = line[:-2]
        elif line[-1:] in CRLF: line = line[:-1]
        return line

    # Internal: get a response from the server, which may possibly
    # consist of multiple lines.  Return a single string with no
    # trailing CRLF.  If the response consists of multiple lines,
    # these are separated by '\n' characters in the string
    def getmultiline(self):
        line = self.getline()
        if line[3:4] == '-':
            code = line[:3]
            while 1:
                nextline = self.getline()
                line = line + ('\n' + nextline)
                if nextline[:3] == code and \
                        nextline[3:4] != '-':
                    break
        return line

	# Internal: get a response from the server.
    # Raise various errors if the response indicates an error
    def getresp(self):
        resp = self.getmultiline()
        if self.debugging: print '*resp*', self.sanitize(resp)
        self.lastresp = resp[:3]
        c = resp[:1]
        if c in ('1', '2', '3'):
            return resp
        if c == '4':
            raise error_temp, resp
        if c == '5':
            raise error_perm, resp
        raise error_proto, resp

    def voidresp(self):
        """Expect a response beginning with '2'."""
        resp = self.getresp()
        if resp[:1] != '2':
            raise error_reply, resp
        return resp

    def abort(self):
        '''Abort a file transfer.  Uses out-of-band data.
        This does not follow the procedure from the RFC to send Telnet
        IP and Synch; that doesn't seem to work with the servers I've
        tried.  Instead, just send the ABOR command as OOB data.'''
        line = 'ABOR' + CRLF
        if self.debugging > 1: print '*put urgent*', self.sanitize(line)
        self.sock.sendall(line, MSG_OOB)
        resp = self.getmultiline()
        if resp[:3] not in ('426', '225', '226'):
            raise error_proto, resp

    def sendcmd(self, cmd):
        '''Send a command and return the response.'''
        self.putcmd(cmd)
        return self.getresp()

    def voidcmd(self, cmd):
        """Send a command and expect a response beginning with '2'."""
        self.putcmd(cmd)
        return self.voidresp()

    def sendport(self, host, port):
        '''Send a PORT command with the current host and the given
        port number.
        '''
        hbytes = host.split('.')
        pbytes = [repr(port//256), repr(port%256)]
        bytes = hbytes + pbytes
        cmd = 'PORT ' + ','.join(bytes)
        return self.voidcmd(cmd)

    def sendeprt(self, host, port):
        '''Send a EPRT command with the current host and the given port number.'''
        af = 0
        if self.af == socket.AF_INET:
            af = 1
        if self.af == socket.AF_INET6:
            af = 2
        if af == 0:
            raise error_proto, 'unsupported address family'
        fields = ['', repr(af), host, repr(port), '']
        cmd = 'EPRT ' + '|'.join(fields)
        return self.voidcmd(cmd)

    def makeport(self):
        '''Create a new socket and send a PORT command for it.'''
        msg = "getaddrinfo returns an empty list"
        sock = None
        for res in socket.getaddrinfo(None, 0, self.af, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
            af, socktype, proto, canonname, sa = res
            try:
                sock = socket.socket(af, socktype, proto)
                sock.bind(sa)
            except socket.error, msg:
                if sock:
                    sock.close()
                sock = None
                continue
            break
        if not sock:
            raise socket.error, msg
        sock.listen(1)
        port = sock.getsockname()[1] # Get proper port
        host = self.sock.getsockname()[0] # Get proper host
        if self.af == socket.AF_INET:
            resp = self.sendport(host, port)
        else:
            resp = self.sendeprt(host, port)
        if self.timeout is not _GLOBAL_DEFAULT_TIMEOUT:
            sock.settimeout(self.timeout)
        return sock

    def makepasv(self):
        if self.af == socket.AF_INET:
            host, port = parse227(self.sendcmd('PASV'))
        else:
            host, port = parse229(self.sendcmd('EPSV'), self.sock.getpeername())
        return host, port

    def ntransfercmd(self, cmd, rest=None):
        """Initiate a transfer over the data connection.

        If the transfer is active, send a port command and the
        transfer command, and accept the connection.  If the server is
        passive, send a pasv command, connect to it, and start the
        transfer command.  Either way, return the socket for the
        connection and the expected size of the transfer.  The
        expected size may be None if it could not be determined.

        Optional `rest' argument can be a string that is sent as the
        argument to a REST command.  This is essentially a server
        marker used to tell the server to skip over any data up to the
        given marker.
        """
        size = None
        if self.passiveserver:
            host, port = self.makepasv()
            conn = socket.create_connection((host, port), self.timeout)
            if rest is not None:
                self.sendcmd("REST %s" % rest)
            resp = self.sendcmd(cmd)
            # Some servers apparently send a 200 reply to
            # a LIST or STOR command, before the 150 reply
            # (and way before the 226 reply). This seems to
            # be in violation of the protocol (which only allows
            # 1xx or error messages for LIST), so we just discard
            # this response.
            if resp[0] == '2':
                resp = self.getresp()
            if resp[0] != '1':
                raise error_reply, resp
        else:
            sock = self.makeport()
            if rest is not None:
                self.sendcmd("REST %s" % rest)
            resp = self.sendcmd(cmd)
            # See above.
            if resp[0] == '2':
                resp = self.getresp()
            if resp[0] != '1':
                raise error_reply, resp
            conn, sockaddr = sock.accept()
            if self.timeout is not _GLOBAL_DEFAULT_TIMEOUT:
                conn.settimeout(self.timeout)
        if resp[:3] == '150':
            # this is conditional in case we received a 125
            size = parse150(resp)
        return conn, size

    def transfercmd(self, cmd, rest=None):
        """Like ntransfercmd() but returns only the socket."""
        return self.ntransfercmd(cmd, rest)[0]

    def login(self, user = '', passwd = '', acct = ''):
        '''Login, default anonymous.'''
        if not user: user = 'anonymous'
        if not passwd: passwd = ''
        if not acct: acct = ''
        if user == 'anonymous' and passwd in ('', '-'):
            # If there is no anonymous ftp password specified
            # then we'll just use anonymous@
            # We don't send any other thing because:
            # - We want to remain anonymous
            # - We want to stop SPAM
            # - We don't want to let ftp sites to discriminate by the user,
            #   host or country.
            passwd = passwd + 'anonymous@'
        resp = self.sendcmd('USER ' + user)
        if resp[0] == '3': resp = self.sendcmd('PASS ' + passwd)
        if resp[0] == '3': resp = self.sendcmd('ACCT ' + acct)
        if resp[0] != '2':
            raise error_reply, resp
        return resp

    def retrbinary(self, cmd, callback, blocksize=8192, rest=None):
        """Retrieve data in binary mode.  A new port is created for you.

        Args:
          cmd: A RETR command.
          callback: A single parameter callable to be called on each
                    block of data read.
          blocksize: The maximum number of bytes to read from the
                     socket at one time.  [default: 8192]
          rest: Passed to transfercmd().  [default: None]

        Returns:
          The response code.
        """
        self.voidcmd('TYPE I')
        conn = self.transfercmd(cmd, rest)
        while 1:
            data = conn.recv(blocksize)
            if not data:
                break
            callback(data)
        conn.close()
        return self.voidresp()

    def retrlines(self, cmd, callback = None):
        """Retrieve data in line mode.  A new port is created for you.

        Args:
          cmd: A RETR, LIST, NLST, or MLSD command.
          callback: An optional single parameter callable that is called
                    for each line with the trailing CRLF stripped.
                    [default: print_line()]

        Returns:
          The response code.
        """
        if callback is None: callback = print_line
        resp = self.sendcmd('TYPE A')
        conn = self.transfercmd(cmd)
        fp = conn.makefile('rb')
        while 1:
            line = fp.readline()
            if self.debugging > 2: print '*retr*', repr(line)
            if not line:
                break
            if line[-2:] == CRLF:
                line = line[:-2]
            elif line[-1:] == '\n':
                line = line[:-1]
            callback(line)
        fp.close()
        conn.close()
        return self.voidresp()

    def storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None):
        """Store a file in binary mode.  A new port is created for you.

        Args:
          cmd: A STOR command.
          fp: A file-like object with a read(num_bytes) method.
          blocksize: The maximum data size to read from fp and send over
                     the connection at once.  [default: 8192]
          callback: An optional single parameter callable that is called on
                    on each block of data after it is sent.  [default: None]
          rest: Passed to transfercmd().  [default: None]

        Returns:
          The response code.
        """
        self.voidcmd('TYPE I')
        conn = self.transfercmd(cmd, rest)
        while 1:
            buf = fp.read(blocksize)
            if not buf: break
            conn.sendall(buf)
            if callback: callback(buf)
        conn.close()
        return self.voidresp()

    def storlines(self, cmd, fp, callback=None):
        """Store a file in line mode.  A new port is created for you.

        Args:
          cmd: A STOR command.
          fp: A file-like object with a readline() method.
          callback: An optional single parameter callable that is called on
                    on each line after it is sent.  [default: None]

        Returns:
          The response code.
        """
        self.voidcmd('TYPE A')
        conn = self.transfercmd(cmd)
        while 1:
            buf = fp.readline()
            if not buf: break
            if buf[-2:] != CRLF:
                if buf[-1] in CRLF: buf = buf[:-1]
                buf = buf + CRLF
            conn.sendall(buf)
            if callback: callback(buf)
        conn.close()
        return self.voidresp()

    def acct(self, password):
        '''Send new account name.'''
        cmd = 'ACCT ' + password
        return self.voidcmd(cmd)

    def nlst(self, *args):
        '''Return a list of files in a given directory (default the current).'''
        cmd = 'NLST'
        for arg in args:
            cmd = cmd + (' ' + arg)
        files = []
        self.retrlines(cmd, files.append)
        return files

    def dir(self, *args):
        '''List a directory in long form.
        By default list current directory to stdout.
        Optional last argument is callback function; all
        non-empty arguments before it are concatenated to the
        LIST command.  (This *should* only be used for a pathname.)'''
        cmd = 'LIST'
        func = None
        if args[-1:] and type(args[-1]) != type(''):
            args, func = args[:-1], args[-1]
        for arg in args:
            if arg:
                cmd = cmd + (' ' + arg)
        self.retrlines(cmd, func)

    def rename(self, fromname, toname):
        '''Rename a file.'''
        resp = self.sendcmd('RNFR ' + fromname)
        if resp[0] != '3':
            raise error_reply, resp
        return self.voidcmd('RNTO ' + toname)

    def delete(self, filename):
        '''Delete a file.'''
        resp = self.sendcmd('DELE ' + filename)
        if resp[:3] in ('250', '200'):
            return resp
        else:
            raise error_reply, resp

    def cwd(self, dirname):
        '''Change to a directory.'''
        if dirname == '..':
            try:
                return self.voidcmd('CDUP')
            except error_perm, msg:
                if msg.args[0][:3] != '500':
                    raise
        elif dirname == '':
            dirname = '.'  # does nothing, but could return error
        cmd = 'CWD ' + dirname
        return self.voidcmd(cmd)

    def size(self, filename):
        '''Retrieve the size of a file.'''
        # The SIZE command is defined in RFC-3659
        resp = self.sendcmd('SIZE ' + filename)
        if resp[:3] == '213':
            s = resp[3:].strip()
            try:
                return int(s)
            except (OverflowError, ValueError):
                return long(s)

    def mkd(self, dirname):
        '''Make a directory, return its full pathname.'''
        resp = self.sendcmd('MKD ' + dirname)
        return parse257(resp)

    def rmd(self, dirname):
        '''Remove a directory.'''
        return self.voidcmd('RMD ' + dirname)

    def pwd(self):
        '''Return current working directory.'''
        resp = self.sendcmd('PWD')
        return parse257(resp)

    def quit(self):
        '''Quit, and close the connection.'''
        resp = self.voidcmd('QUIT')
        self.close()
        return resp

    def close(self):
        '''Close the connection without assuming anything about it.'''
        if self.file:
            self.file.close()
            self.sock.close()
            self.file = self.sock = None

