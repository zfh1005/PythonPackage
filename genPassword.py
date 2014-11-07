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
  for i in range(100000):
    writeLog(LOG_PATH, genPassword(16))
  print(time.time() - start, '\nFinish')  
    