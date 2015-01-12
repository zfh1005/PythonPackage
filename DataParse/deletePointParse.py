# -*- coding: utf-8 -*-

#!/usr/bin/env python
'''
If a file's every line start with '.', delete the '.' and the content before the '.'
'''

import os
import sys


PARSE_PATH = 'D:\\Temp\\temp.txt'
LOG_PATH = 'd:\\result.txt'

#parse test data
#the param sourcePathath is filePath need parse
def parseData(sourcePath):
    returnResult = ''
    value = ['']
    
    f = open(sourcePath, 'r')
    try:
        lines = f.readlines()
        for line in lines:
            p = line.split('.')[1:]
            #print('p ', p)
            value += p
    except:
        pass
    
    finally:    
        f.close       
  
    #print('value ', value)
    for x in value :
        returnResult += x 
    #print('returnResult', returnResult)
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
        filePathNeedParse = PARSE_PATH
    else:
        filePathNeedParse = sys.argv[1]
    
    writeLog(LOG_PATH,  parseData(filePathNeedParse))   
        