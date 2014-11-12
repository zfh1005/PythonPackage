# -*- coding: utf-8 -*-

#!/usr/bin/env python

import os
import re
import time as timeTime
import sys

SETTING_FILE = ['mySetup.ini']
PARSE_PATH = ['D:\\Temp\\log', 'D:\\log']
OUTPUT_FOLDER = 'D:\\RokuFileChangeList\\'

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
                    writeData(genRecordFileName(), result)
    print('finish!')
    pass

#parse test data
#the param sourcePathath is filePath need parse
def parseData(sourcePath):
    returnResult = ''
     #add record mySetup file open time 
    nowTime = 'NowTime: ' + timeTime.strftime('%Y-%m-%d %H:%M:%S', timeTime.localtime())
    #add record mySetup file modfiy time 
    tempTime = timeTime.strftime('%Y-%m-%d %H:%M:%S', timeTime.localtime(os.path.getmtime(sourcePath.strip())))
    ModfiyTime = 'ModfiyTime: ' + tempTime
    fileFolder = sourcePath.split('\\')[-2].strip()
    value = [sourcePath.strip(), fileFolder, nowTime, ModfiyTime]
    start = timeTime.time()
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
        
    #print(timeTime.time() - start)
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

def genRecordFileName():
    tempFileName = OUTPUT_FOLDER + 'recardChangeList' + timeTime.strftime('%Y-%m-%d_%H-%M-%S', timeTime.localtime()) + '.txt'
    if not os.path.exists(tempFileName):
        os.makedirs(OUTPUT_FOLDER, exist_ok = True)
    return tempFileName

if __name__=="__main__":   
    if len(sys.argv) < 2:
        listForderFileList(PARSE_PATH) 
    else:
        listForderFileList(sys.argv)     
        
    