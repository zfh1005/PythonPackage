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

	
def getErrorCode(e):
    assert len(e) != 0
    errorCode = ''
    #e = ['8.TX_VERIFY_EVM 2472 MCS7 HT20 _FREQ', '-25.00', '-1.66', ' 25.00']
    ErrorList = e[0].split(' ')
    #ErrorList = ['8.TX_VERIFY_EVM', '2472', 'MCS7', 'HT20', '_FREQ']
    if '_EVM' in ErrorList[-1]:
        errorCode += 'EV'
        if '24' in ErrorList[1]:
            errorCode += '04'
        else:
            errorCode += '14'
    elif '_POWER' in ErrorList[-1]:
        errorCode += 'PW'
        if '24' in ErrorList[1]:
            errorCode += '04'
        else:
            errorCode += '14'
    elif 'FREQ' in ErrorList[-1]:
        errorCode += 'FQ'
        if '24' in ErrorList[1]:
            errorCode += '04'
        else:
            errorCode += '14'
    elif 'PER' in ErrorList[-1]:
        errorCode += 'PR'
        if '24' in ErrorList[1]:
            errorCode += '04'
        else:
            errorCode += '14'
    elif 'MASK' in ErrorList[-1]:
        errorCode += 'MS'
        if '24' in ErrorList[1]:
            errorCode += '04'
        else:
            errorCode += '14'
    elif '_IQ' in ErrorList[-1]:
        errorCode += 'SY00'
    elif '_TT00' in ErrorList[-1]:
        errorCode += 'TT00'
    elif '_EX01' in ErrorList[-1]:
        errorCode += 'EX01'     
    return  errorCode