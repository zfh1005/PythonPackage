#!/usr/bin/env python
import os
import re
import time
from os.path import join, getsize

TXT_FILE_EXT = ['txt', 'log']
PARSE_PATH = 'd:\\360'
LOG_PATH = 'd:\\1.txt'

#user os.walk list all txt/log file in forder
#the param name is the forder name
def listForderFileList(name):
    size = 0
    temp = ''
    for root, dirs, files in os.walk(name):
        for dn in  dirs:
            #pass
            print('Forder:  ' + join(root, dn))
                  
        for fn in files:
            pass
        '''    
            size += sum([getsize(join(root, name)) for name in files])
        temp += join(root, name) + '\t' + str(size)
        writeLog(LOG_PATH, size)
        '''
    pass



#write data to log file
#param logPath is write log file path
#param result is the data need to write
def writeLog(logPath, result):
    f = open(logPath, 'a+')
    f.write(str(result) + '\n')
    f.flush
    f.close
    
    
class dir(object):
    def __init__(self): 
        self.CONST =0 
        self.SPACE ="" 
        self.list =[]
        
    def p(self,url):
        myfile = ''
        files = os.listdir(url) 
        for file in files: 
            myfile = url + "\\"+file 
            size = os.path.getsize(myfile) 
        if os.path.isfile(myfile): 
            self.list.append(str(self.SPACE)+"|____"+file +" "+ str(size)+"\n") 
            # print str(self.SPACE)+"|____"+file +" "+ str(size) 
        
        if os.path.isdir(myfile) : 
            self.list.append(str(self.SPACE)+"|____"+file + "\n") 
        #get into the sub-directory,add "| " 
        self.SPACE = self.SPACE+"| " 
        self.p(myfile) 
        #when sub-directory of iteration is finished,reduce "| " 
        self.SPACE = self.SPACE[:-5] 
        return self.list

    def writeList(self,url): 
        f = open(url,'w') 
        f.writelines(self.list) 
        print ("ok" )
        f.close() 


#if '__name__' == '__main__':     
#p = listForderFileList(PARSE_PATH)
d = dir()
d.p(PARSE_PATH)
d.writeList(LOG_PATH)
