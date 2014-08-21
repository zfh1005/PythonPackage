import os
import time
import codecs

File_PATH = 'd:\\result.txt'
File_PATH1 = 'd:\\result1.txt'

def FileReplace(f):
    ff = codecs.open(f, 'r')
    lines = ff.readlines()
    temp = ''
    for line in lines:
        #print(line)
        temp += str(line).replace('.', '')
        
    ff.close()
    #del(f)  
    writeData( temp) 

#write d to file
#param f the file name 
#param d the data need to write
def writeData( d):
    #used unicode open file
    ff = codecs.open(File_PATH1, 'w', 'utf-8')
    ff.write(d)
    ff.flush
    ff.close


if __name__ == '__main__':
    start = time.time()
    FileReplace(File_PATH)
    print(time.time() - start)   