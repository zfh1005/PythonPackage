
import os
import os.path
import shutil
import time

L_PATH = 'D:\\LogBackup'  
S_PATH = 'f:\\temp'
SN_PATH = 'd:\\temp\\SN.txt'


#open SN file and get SN into a list
#param f the file name contant SN
def getSNList(f):
    SNList = []
    #open SN file to read
    ff = open(f, 'r')
    lines = ff.readlines()
    for line in lines:
        temp = line.split('\\t')
        i = 0
        while i < len(temp):
            #print(temp[i])
            #get SN list
            if len(temp[i].split('\n')[0]) == 12 :
            #if re.compile('^\\d\\w{11}', temp[i]) :
                SNList.append(temp[i].split('\n')[0])
            i += 1  
    return SNList      

#operation list initalize a dictionary with SN:first_find_path
#param l the list operation
def getSNDicts(l):
    #initalize a dictionary
    dataDicts = {}
    for s in l:
        #insert data to dataDicts
        temp = '201' + s[3] + '0' + s[4]
        dataDicts[s] = temp
    #print(dataDicts)
    return dataDicts

#find file  
#param l the SN list
#param d the SN dictionary
#param s the server file log path  
#param n the forlder name to save found file
def FindFile(l, d, s, n):
     for root, dirs, files in os.walk(s):
        i = 0
        while(i < len(l)):
            for dir in dirs:
                #dictionary's value in current path
                if not d[l[i]] in dir:
                    break;
                else:
                    #print(os.path.join(root, dir))
                    FindFile2(os.path.join(root, dir), l, d, s, n)
            i += 1
            
            '''
            for fn in files:
                print(os.path.join(root, fn))
                if(os.path.join(root, fn)):
                    pass
                
                #file name in list
                if(fn.split('.')[0] in l):
                    #get current file full path
                    ff = os.path.join(root, fn)
                    #print(ff)
                    #get recard file path tree
                    tt = ff.replace(ff.split('\\')[0], n)
                    #print(tt)
                    #the path not exits, creat the tree
                    if not os.path.exists(tt.split(fn)[0]):
                        #print(tt.split(fn)[0])
                        os.makedirs(tt.split(fn)[0])
                    #copy file to another forlder
                    CopyFile(ff, tt)
            '''

#traverse file list and copy need file
#param p the find path
#param l the SN list
#param d the SN dictionary
#param s the server file path  
#param n the forlder name to save found file
def FindFile2(p, l , d, s, n):
    #get file list in p
    names = os.listdir(p)
    for name in names:
        temp = os.path.join(p, name)
        if(os.path.isfile(temp)):
            #print(temp)
            i = 0
            while(i < len(l)):
                if(name.split('.')[0] in l[i]):
                    #get recard file path tree
                    tt = temp.replace(temp.split('\\')[0], n)
                    #print(tt)
                    #the path not exits, creat the tree
                    if not os.path.exists(tt.split(name)[0]):
                        #print(tt.split(fn)[0])
                        os.makedirs(tt.split(name)[0])
                    #copy file to another forlder
                    CopyFile(temp, tt)
                else:
                    pass
                i += 1    
        elif(os.path.isdir(name)):
            FindFile2(os.path.join(p, name), l, d, s, n)
                    
#copy file from f to t
#param f is full file name need to copy 
#param t is full file name copy to path            
def CopyFile(f, t):
    if not os.path.isfile(f) and  not os.path.isfile(t):
        return
    #copy file from f to t
    shutil.copy2(f, t)  
        



if __name__ == '__main__':
    
    start = time.time()
    sn = getSNList(SN_PATH)
    #print(sn)
    snDicts = getSNDicts(sn)
    #print(snDicts)
    
    if not os.path.isdir(L_PATH):
        os.mkdir(L_PATH)
    FindFile(sn, snDicts, S_PATH ,L_PATH)
    print(time.time() - start)
  