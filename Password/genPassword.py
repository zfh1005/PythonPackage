# -*- coding: utf-8 -*-
import string
import random
import time

LOG_PATH = 'd:\\result.txt'

'''
Function is genPassword
param length is the password lenght.Default leght is 8.
param chars is the random range.Default range is lowercase letters, uppercase letters and digits.
'''
def genPassword(length=8,chars=string.digits+string.ascii_letters):
    return ''.join(random.sample(chars*10,length))

def writeLog(logPath, result):
    f = open(logPath, 'a')
    f.write(str(result) + '\n')
    f.flush
    f.close

if __name__=="__main__":
  start = time.time()
  for i in range(1, 100000):
    writeLog(LOG_PATH, (str(i).ljust(10, ' ')) + (genPassword(16)))
  print(time.time() - start, '\nFinish')  
    
'''
字符串在输出时的对齐：
S.ljust(width,[fillchar])   
#输出width个字符，S左对齐，不足部分用fillchar填充，默认的为空格。  
S.rjust(width,[fillchar]) #右对齐  
S.center(width, [fillchar]) #中间对齐  
S.zfill(width) #把S变成width长，并在右对齐，不足部分用0补足   
'''    