#encoding: UTF-8

ERROR_CODE_DEFINE_FILE_NAME = r'WiFiErrorCodeDefine.txt'

def parseErrorCodeDefine():
    f = open(ERROR_CODE_DEFINE_FILE_NAME, 'r')
    lines = f.readlines()
    for line in lines:
        tempKey = line.strip().split(':')[0].strip()
        tempValue = line.strip().split(':')[-1].strip()
        ErrorCodeDict[tempKey] = tempValue
    return ErrorCodeDict
