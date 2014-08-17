import subprocess

cmd = 'cmd.exe'
begin = 0
end = 255
while begin < end:
    p = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    p.stdin.write('ping 192.168.1.' str(begin) + '\n')
    p.stdin.close()
    p.wait()
    print('result: %s' %p.stdout.read())
    
    