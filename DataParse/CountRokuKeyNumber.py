# -*- coding: utf-8 -*-

#!/usr/bin/env python
import os
import sys

PARSE_PATH = 'D:\\Temp\\log'

#user os.walk list all txt/log file in forder
#the param name is the forder name
def listForderFileList(name):
    num = 0
    #parser all file path
    for root, dirs, files in os.walk(name):
        for fn in files:
            if(fn.split('.')[-1].strip() == 'dat'):
                num += 1
    print(num)

    
if __name__=="__main__":   
    if len(sys.argv) < 2:
        listForderFileList(PARSE_PATH) 
    else:
        listForderFileList(sys.argv[1])         