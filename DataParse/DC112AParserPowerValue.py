# -*- coding: utf-8 -*-

#!/usr/bin/env python
import os
import re
import time
import sys

TXT_FILE_EXT = ['txt', 'log']
PARSE_PATH = 'D:\\Temp\\log'
LOG_PATH = 'd:\\result.xls'

#user os.walk list all txt/log file in forder
#the param name is the forder name
def listForderFileList(name):
    start = time.time()
    for root, dirs, files in os.walk(name):
        for fn in files:
            if(fn.split('.')[-1] in TXT_FILE_EXT):
                filename = root + '\\' + fn
                #parse data
                result = parseData(filename)
                writeLog(LOG_PATH, result)
    print('finish!')
    print(time.time() - start)
    pass


#parse test data
#the param sourcePathath is filePath need parse
def parseData(sourcePath):
    returnResult = ''
    value = [sourcePath.strip(), sourcePath.split('\\')[-1].split('.')[0].strip()]
    
    f = open(sourcePath, 'r')
    try:
        lines = f.readlines()
        for line in lines:
            if('power meter' in line):
                p = line.strip().split('::')[-1]
                #print(p)
                value.append(p)
    except:
        pass
    finally:    
        f.close       
    
    #print(value)
    iNum = 0
    for x in value :
        iNum += 1        
        if '\t' in x:
            returnResult += x
        else:
            returnResult += x + '\t'
        if ((iNum - 2) % 8  == 0):
            if '\n' not in x:
                returnResult += '\n'    
    return returnResult

#write data to log file
#param logPath is write log file path
#param result is the data need to write
def writeLog(logPath, result):
    f = open(logPath, 'a')
    f.write(str(result) + '\n')
    f.flush
    f.close

if __name__=="__main__":   
    if len(sys.argv) < 2:
        listForderFileList(PARSE_PATH) 
    else:
        listForderFileList(sys.argv[1])     
        
    
