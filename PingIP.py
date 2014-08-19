import subprocess

cmd = 'cmd.exe'
begin = 0
end = 255
while begin < end:
    begin += 1
    p = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    temp = 'ping 192.168.1.' + str(begin) + ' -n 2'+'\n'
    p.stdin.write(temp.encode('utf-8'))
    #p.stdin.write("ping 192.168.1."+str(begin)+"\n")  
    p.stdin.close()
    p.wait(100)
    rst = p.stdout.read()
    print('%s' %rst.decode('gbk'))
    p.stdout.close()
    
    
