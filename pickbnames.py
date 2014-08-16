import os 
LOGFILEPSTH = 'c:\\names.txt'
filenames = os.listdir(os.getcwd())
for name in filenames:
    filenames[filenames.index(name)] = name[:-3]
out = open(LOGFILEPSTH, 'w')
for name in filenames:
    out.write(name + '\n')
out.close()    
