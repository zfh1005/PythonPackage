import math
import os 
import sys

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

def CoverMACToNumber(mac):
    if len(mac) != 12:
        #right format the mac
        mac = mac.rjust(12, '0')
        '''
        for i in range(0, 12 - len(mac)):
            temp = mac[::-1] + '0'
            mac = temp[::-1]
        '''    
    i = 0
    Number = 0
    while(i < 12):
        temp = CoverCharToNum(mac[::-1][i])
        Number += math.pow(16, i) * temp
        i += 1
    return Number
    

def CoverCharToNum(ch):
    Numner = 0
    str1 = ['a', 'b', 'c', 'd', 'e', 'f']
    if ch in ['0', '1', '2', '3', '4', '5', '6', '7' '8' '9']:
        Numner = int(ch.lower())
    if ch in str1:
        Numner = str1.index(ch.lower()) + 10
    '''
    if ch.lower() == 'a':
        temp = 10
    elif ch.lower() == 'b':
        temp = 11
    elif ch.lower() == 'c':
        temp = 12
    elif ch.lower() == 'd':
        temp = 13
    elif ch.lower() == 'e':
        temp = 14
    elif ch.lower() == 'f':
        temp = 15
   '''
    return Numner        
  
def CoverNumberToMac(number):
    MAC = ''
    num = int(number)
    while True:
        if num == 0: 
            break
        num,rem = divmod(num, 16)
        MAC += CoverNumberToChar(rem)
    return MAC[::-1]
    
def CoverNumberToChar(i):
    print(i)
    char = ''
    str1 = ['0', '1', '2', '3', '4', '5', '6', '7' '8' '9','A', 'B', 'C', 'D', 'E', 'F']
    if i >= 0 and i <= 15:
        char = str1[i]
    return char

def hex2dec(string_num):
    return str(int(string_num.upper(), 16))

def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])



MMAC = 'ffffffabcdef'
print(MMAC)     
mac = hex2dec(MMAC)    
print(mac)
mac1 = int(mac) + 3
MAC = dec2hex(mac1)
print(MAC)
            