# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
delete all link file at all desk
'''

import os
import sys
import time

TXT_FILE_EXT = ['lnk']
_PATH = []

#user os.walk list all txt/log file in forder
#the param name is the forder name
def listForderFileList(name):
    start = time.time()
    for root, dirs, files in os.walk(name):
        for fn in files:
            #check file type is '.lnk'
            if(fn.lower().split('.')[-1] in TXT_FILE_EXT):
                filename = root + '\\' + fn
                #delete '.lnk' file
                try:
                    print('filename ', time.time(), filename)
                    os.remove(filename)
                    os.unlink(filename)
                except:
                    pass
                    
    print('finish!')
    print(time.time() - start)
    pass

#get all desk list.(Need change. Get system's desk list, not common)
def deskList():
    #for x in string.ascii_uppercase:
    for x in 'ABDEFGHIJKLMNOPQRSTUVWXYZ':
        _PATH.append(x + ':\\')

if __name__=="__main__":
    for x in _PATH:
        listForderFileList(x)    
    
        