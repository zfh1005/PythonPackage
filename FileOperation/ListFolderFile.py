
#############################################
#   Written Fa-Hong zhou                     #     
#   2015-01-30                               #
#   get folder file list, result in test.xml #
#############################################

import os

LOG_PATH = r'd:\result111.xml'

def getfilelist(filepath, tabnum = 1):
    simplepath = os.path.split(filepath)[1]
    returnstr = simplepath+" Folder<>"+"\n"
    returndirstr = ""
    returnfilestr = ""
    try:
        filelist = os.listdir(filepath)
        for num in range(len(filelist)):
            filename = filelist[num]
            if os.path.isdir(filepath + "/"+filename):
                returndirstr += "\t"*tabnum + getfilelist(filepath + "/" +filename, tabnum + 1)
            else:
                returnfilestr += "\t"*tabnum + filename+"\n"
        returnstr += returnfilestr + returndirstr
        writeLog(returnstr)
    except:
        pass
    return returnstr+"\t"*tabnum + "</>\n"
            
def writeLog(value):
    o=open(LOG_PATH,"a+")
    o.writelines(value)
    o.close()

path = input("Please input a path name:")
usefulpath = path.replace('\\', '/')
if usefulpath.endswith("/"):
    usefulpath = usefulpath[:-1]
if not os.path.exists(usefulpath):
    print("path name error !")
elif not os.path.isdir(usefulpath):
    print("path name is not a path!")
else:
    filelist = os.listdir(usefulpath)
    getfilelist(usefulpath)
    #o=open(LOG_PATH,"w+")
    #o.writelines(getfilelist(usefulpath))
    #o.close()
    print("Success, please check the test.xml file")
