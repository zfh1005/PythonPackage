import os
import os.path
import codecs
import time

Log_Path = 'f:\\temp'
New_Path = 'd:\\temp'

#traverse the path s 
#param s the traverse file name
def ListFile(s):
    for root, dirs, files in os.walk(s):
        for file in files:
            #just operation file name lenght is 12
            if(len(file.split('.')[0]) == 12):
                #get current file's full name
                temp = os.path.join(root, file)
                deleteLine(temp)
            
#delete excess '\r\n' at file
#param f the file name to operation
def deleteLine(f):
    temp = New_Path + '\\' + f.split('\\')[-1]
    #if record file path not exists, create it 
    if not os.path.exists(New_Path):
        os.makedirs(New_Path)
    #used unicode open file
    ff = codecs.open(f, 'r', 'utf-8')
    lines = ff.readlines()
    #print(lines)
    i = 0
    while(i < len(lines)):
        #print(lines[i])
        if '\\r\\n' in lines[i]:
            #replace excess '\r\n' with ''
            lll = lines[i].replace('\\r\\n', '')
            #write new file
            writeData(temp, lll)
        else:
            #writeData(temp, lines[i])
            pass
            
        i += 1
    ff.close()    
    

#write d to file
#param f the file name 
#param d the data need to write
def writeData(f, d):
    #used unicode open file
    ff = codecs.open(f, 'a', 'utf-8')
    ff.write(d)
    ff.flush
    ff.close
    

if __name__ == '__main__':
    start = time.time()
    ListFile(Log_Path)
    print(time.time() - start)
    
    