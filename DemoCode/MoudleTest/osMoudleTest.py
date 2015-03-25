import os

def fileDateDict(path):
    date_from_name = {}
    for name in os.listdir(path):
        fullname = os.path.join(path, name)
        if os.path.isfile(fullname):
            date_from_name[fullname] = os.path.getmtime(fullname)
    return date_from_name        
