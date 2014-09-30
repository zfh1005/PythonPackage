import os
import os.path
import shutil
import time

#copy file and path from 'src' to 'dst'
def copytree(src, dst, symlinks=False):
    
    #if 'src' path is empty, create it
    if not os.path.isdir(dst):
        os.makedirs(dst)
        
    errors = []
    names = os.listdir(src)
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            #srcname is a link
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            #srcname is a path
            elif os.path.isdir(srcname):
                #call the function again
                copytree(srcname, dstname, symlinks)
            #srcname is a file
            else:
                #dstname is a path, delete old and create a new one
                if os.path.isdir(dstname):
                    os.rmdir(dstname)
                #dstname is a file, delete old and create a new one
                elif os.path.isfile(dstname):
                    os.remove(dstname)
                #copy the file
                shutil.copy2(srcname, dstname)            
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except OSError as err:
            errors.extend(err.args[0])
    

def timeToCopy(year = 1970, month = 1, day = 1, hour = 1, minutes = 1):
    lt = time.localtime()
    if(lt.tm_year == year & lt.tm_mon == month & lt.tm_mday == day & lt.tm_hour == hour & lt.tm_min == minutes):
        copytree(S_PATH, L_PATH)    

   
if __name__ == '__main__':
    timeToCopy(2014, 8, 1, 8, 0 )
    #copytree(S_PATH, L_PATH)



S_PATH = 'f:\\temp'
L_PATH = 'D:\\LogBackup'
#copytree(S_PATH, L_PATH)

