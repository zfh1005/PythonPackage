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
	