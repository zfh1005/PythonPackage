#encoding: UTF-8

#!/usr/bin/env python

from xml.dom import minidom, Node

TEST_DATA_LIST_DICT = {'006.004.TX_VERIFY_EVM 2457 MCS7 HT20 #17 $-28 @2 _EVM _POWER': ['-14.99'], '003.TX_VERIFY_EVM 2412 MCS7 HT20 #16.5 $-28 @1 _POWER': ['17.21'], '004.TX_VERIFY_EVM 2457 MCS7 HT20 #17 $-28 @2 _EVM': ['-22.49'], '001.TX_VERIFY_EVM 2412 MCS7 HT20 #16.5 $-28 @1 _EVM': ['-31.34'], '002.TX_VERIFY_EVM 2412 MCS7 HT20 #16.5 $-28 @1 _FREQ': ['-16.22'], '005.004.TX_VERIFY_EVM 2457 MCS7 HT20 #17 $-28 @2 _EVM _FREQ': ['-16.4']}
ERROR_INFO_LIST = ['PW14', '5G POWER test failed', '9.66']

def generateTestReport(dataDict, errorList):
    doc = minidom.Document()

    #generate the 'TestReport'
    testReport = doc.createElement('TestReport')
    doc.appendChild(testReport)

    #the testresult
    testResult = doc.createElement('TestResult')
    tempResult = ''
    if len(errorList) == 0:        
        tempResult = 'PASS'
    else:
        tempResult = 'FAIL'
    testResult.appendChild(doc.createTextNode(tempResult))
    testReport.appendChild(testResult)

    #the testdata
    testData = doc.createElement('TestData')
    testReport.appendChild(testData)

    #the testdata.DataElement
    for x in range(0, len(dataDict)):        
        tempNum = '%03d.'%(x + 1)
        for key in dataDict.keys():
            if tempNum in key:
                dataElement = doc.createElement('DataElement')
                dataElement.setAttribute('key', key)
                dataElement.appendChild(doc.createTextNode(dataDict[key][0]))
                testData.appendChild(dataElement)

    #the errorinfos
    errorinfos = doc.createElement('ErrorInfos')
    testReport.appendChild(errorinfos)

    if len(errorList) != 0:
        #the errorinfos.errorinfo
        errorinfo = doc.createElement('ErrorInfo')
        errorinfos.appendChild(errorinfo)

        #the errorinfos.errorinfo.errorCode
        errorCode = doc.createElement('ErrorCode')
        errorCode.appendChild(doc.createTextNode(errorList[0]))
        errorinfo.appendChild(errorCode)

        #the errorinfos.errorinfo.errorDes
        errorDes = doc.createElement('ErrorDescription')
        errorDes.appendChild(doc.createTextNode(errorList[1]))
        errorinfo.appendChild(errorDes)

        #the errorinfos.errorinfo.errorValue
        errorValue = doc.createElement('ErrorValue')
        errorValue.appendChild(doc.createTextNode(errorList[2]))
        errorinfo.appendChild(errorValue)
    else:
        pass

    return doc.toprettyxml()

if __name__ == '__main__':
    print(generateTestReport(TEST_DATA_LIST_DICT, ERROR_INFO_LIST))
