# -*- coding: utf-8 -*-

#!/usr/bin/env python

import os
import re
import time
import sys

SETTING_FILE = ['mySetup.ini']
PARSE_PATH = ['D:\\Temp\\log', 'D:\\log']
LOG_PATH = 'd:\\ChangeList.txt'

#user os.walk list all txt/log file in forder
#the param name is the forder name
def listForderFileList(names):
    #parser all file path
    for name in names:
        for root, dirs, files in os.walk(name):
            for fn in files:
                if(fn in SETTING_FILE):
                    filename = root + '\\' + fn
                    #parse data
                    result = parseData(filename)
                    writeLog(LOG_PATH, result)
    print('finish!')
    pass

#parse test data
#the param sourcePathath is filePath need parse
def parseData(sourcePath):
    returnResult = ''
    value = [sourcePath.strip(), sourcePath.split('\\')[-1].strip()]
    start = time.time()
    f = open(sourcePath, 'r')
    try:
        lines = f.readlines()
        tempBool = False
        for line in lines:
            #parser test station
            if 'TestStation' in line:
                p = line.split('=')[-1].strip()
                #print(p)
                value.append(p) 
            #parser DHCPMAC    
            elif(('DHCPMAC' in line) or ('MacPrefix1' in line) or ('MacPrefix2' in line) or ('MacControl' in line)):
                p = line.strip()
                #print(p)
                value.append(p)
            #parser project name    
            elif(('[' in line) and (']' in line) and ('.' in line) ) :
                tempBool = True
                p = line.strip()
                #print(p)
                value.append(p)
            #parser SW version
            elif (('SwVersion' and 'Linux' in line) and ('SwVersionSteven' not in line) and ('WiFiSwVersion' not in line)):
                if tempBool == True :
                    p = line.strip()
                    #print(p)
                    value.append(p)  
                    tempBool = False
            #parser SN prefix and key prefix
            elif(('SnPrefix' in line) and ('KeyFilePath' in line)):
                if tempBool == True :
                    p = line.strip()
                    #print(p)
                    value.append(p)
                    tempBool = False 
    except:
        pass
    finally:    
        f.close
        
    #print(time.time() - start)
    #print(value)
    for x in value :
        if '\n' in x:
            returnResult += x
        else:
            returnResult += x + '\n'
    return returnResult

#write data to log file
#param logPath is write log file path
#param result is the data need to write
def writeData(logPath, result):
    f = open(logPath, 'a')
    f.write(str(result) + '\n')
    f.flush
    f.close

if __name__=="__main__":   
    if len(sys.argv) < 2:
        listForderFileList(PARSE_PATH) 
    else:
        listForderFileList(sys.argv[1])     
        
    