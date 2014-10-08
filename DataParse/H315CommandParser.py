#!/usr/bin/env python
import os
import re
import time

TXT_FILE_EXT = ['txt', 'log', 'pl']
PARSE_PATH = 'D:\\Temp\\log'
LOG_PATH = 'd:\\result.txt'

#user os.walk list all txt/log file in forder
#the param name is the forder name
def listForderFileList(name):
    for root, dirs, files in os.walk(name):
        for fn in files:
            if(fn.split('.')[-1] in TXT_FILE_EXT):
                filename = root + '\\' + fn
                #parse data
                result = parseData(filename)
                writeLog(LOG_PATH, result)
    print('finish!')
    pass


#parse test data
#the param sourcePathath is filePath need parse
def parseData(sourcePath):
    returnResult = '\t'
    value = [sourcePath]
    start = time.time()
    f = open(sourcePath, 'r')
    lines = f.readlines()
    for line in lines:
        if('wl -i' in line):
            p = ""
            if "#" in line:
                p = line.split('#')[-1]
            else:
                p = line
            print(p)
            value.append(p)
    f.close
    print(time.time() - start)
    
    for x in value :
        if '\r\n' in x:
            returnResult += x
        else:
            returnResult += x + '\r\n'
    return returnResult

#write data to log file
#param logPath is write log file path
#param result is the data need to write
def writeLog(logPath, result):
    f = open(logPath, 'a')
    f.write(str(result) + '\n')
    f.flush
    f.close
   
p = listForderFileList(PARSE_PATH) 
