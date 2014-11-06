# -*- coding: utf-8 -*-
import string
import random

'''
Function is genPassword
param length is the password lenght.Default leght is 8.
param chars is the random range.Default range is lowercase letters, uppercase letters and digits.
'''
def genPassword(length=8,chars=string.digits+string.ascii_letters):
    return ''.join(random.sample(chars*10,length))

if __name__=="__main__":
  for i in range(100000):
    print(genPassword(16))