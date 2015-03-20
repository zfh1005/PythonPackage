import os
import sys
import time
import traceback
import threading as Thread

FILE_PATH = 'E:\Project\Python\RokuFileParition\ind4205EUMay1522176_5.dat'
FILE_SZIE = 16384
RENAME_FLAF = 1

def filePartition(path, size, flag):
    startTime = time.time()
    print('Start test time: ' + time.strftime('%Y/%m/%d %H:%M:%S'))
    if not os.path.exists(path):
        print('\"%s\" not exits, please check.'%path)

    f = open(path, 'rb')
    i = 1
    fileSize = os.path.getsize(path)
    while True:
        newFilePath = r'%s\%s_%d'%(os.path.abspath(os.path.dirname(path)), 'key', FILE_SZIE)
        if not os.path.exists(newFilePath):
            os.makedirs(newFilePath)

        newFileName = r'%s\%s_%d.%s'%(newFilePath, path.split('\\')[-1].split('.')[0], i, path.split('.')[-1])        
        buffer = f.read(int(size))
        f.seek(i * int(size), 0)
        if len(buffer) != 0:
            writeFile(newFileName, buffer)
            if int(flag) == 1:                
                renameFile(newFileName)
            i = i + 1
        if not buffer:
            break
    print('The total number is : %s'%(i-1))
    print('Finished test time: ' + time.strftime('%Y/%m/%d %H:%M:%S'))
    print('Test time: %0.2f'%(time.time() - startTime))


def writeFile(e, w):
    try:
        f = open(e, 'wb')
        f.write(w)
        f.flush()
        f.close()
    except:
        traceback.print_exc()

def renameFile(e):
    try:
        f = open(e, 'rb')
        buffer = f.read(12)
        f.close()
        newFileName = r'%s\%s.%s'%(os.path.abspath(os.path.dirname(e)), buffer.decode(), e.split('.')[-1])        
        os.rename(e, newFileName)
    except:
        traceback.print_exc()


class splitThread(Thread):
    def __init__(self, threadName, fileName, fileSize, filePostion):
        self.threadName = threadName
        self.fileName = fileName
        self.fileSize = fileSize
        self.filePostion = filePostion
        
    def run(self):
        pass
        


  
if __name__ == '__main__':
    if len(sys.argv) < 4:        
        filePartition(FILE_PATH, FILE_SZIE, RENAME_FLAF)
    else:
        filePartition(sys.argv[1], sys.argv[2], sys.argv[3])
   
