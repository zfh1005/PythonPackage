#encoding: UTF-8

#!/usr/bin/env python

from xml.dom import minidom, Node

TEST_DATA_LIST_DICT = {'025.RX_VERIFY_PER 2472 MCS0 HT20 _PER': ['0', '0.00', ' 10.00'], '018.TX_VERIFY_EVM 5825 MCS7 HT20 _EVM': ['-99', '-29.75', ' -28.00'], '027.RX_VERIFY_PER 5180 MCS0 HT20 _PER': ['0', '0.00', ' 10.00'], '029.RX_VERIFY_PER 5825 MCS7 HT20 _PER': ['0', '0.00', ' 10.00'], '015.TX_VERIFY_EVM 5180 MCS7 HT20 _FREQ': ['-20.00', '-1.75', ' 20.00'], '008.TX_VERIFY_EVM 2412 MCS7 HT20 _POWER': ['11.00', '14.66', ' 18.00'], '017.TX_VERIFY_MASK 5180 MCS7 HT20 _MASK': ['0', '0.00', '99'], '031.REMOVE_DUT _IQ': ['-99', '-99', '-99'], '030.DISCONNECT_IQ_TESTER _IQ': ['-99', '-99', '-99'], '003.INSERT_DUT _IQ': ['-99', '-99', '-99'], '028.RX_VERIFY_PER 5825 MCS0 HT20 _PER': ['0', '0.00', ' 10.00'], '013.TX_VERIFY_MASK 2472 MCS7 HT20 _MASK': ['0', '0.00', '99'], '007.TX_VERIFY_EVM 2412 MCS7 HT20 _FREQ': ['-25.00', '-1.69', ' 25.00'], '002.CONNECT_IQ_TESTER _IQ': ['-99', '-99', '-99'], '011.TX_VERIFY_EVM 2472 MCS7 HT20 _FREQ': ['-25.00', '-1.66', ' 25.00'], '016.TX_VERIFY_EVM 5180 MCS7 HT20 _POWER': ['11.00', '13.19', ' 18.00'], '009.TX_VERIFY_MASK 2412 MCS7 HT20 _MASK': ['0', '0.00', '99'], '014.TX_VERIFY_EVM 5180 MCS7 HT20 _EVM': ['-99', '-33.44', ' -28.00'], '005.LOAD_PATH_LOSS_TABLE _IQ': ['-99', '-99', '-99'], '001.GLOBAL_SETTINGS _IQ': ['-99', '-99', '-99'], '024.RX_VERIFY_PER 2472 MCS7 HT20 _PER': ['0', '0.00', ' 10.00'], '019.TX_VERIFY_EVM 5825 MCS7 HT20 _FREQ': ['-20.00', '-1.77', ' 20.00'], '010.TX_VERIFY_EVM 2472 MCS7 HT20 _EVM': ['-99', '-32.44', ' -28.00'], '006.TX_VERIFY_EVM 2412 MCS7 HT20 _EVM': ['-99', '-31.44', ' -28.00'], '023.RX_VERIFY_PER 2412 MCS0 HT20 _PER': ['0', '0.00', ' 10.00'], '021.TX_VERIFY_MASK 5825 MCS7 HT20 _MASK': ['0', '0.05', '99'], '022.RX_VERIFY_PER 2412 MCS7 HT20 _PER': ['0', '0.00', ' 10.00'], '032.RUN_EXTERNAL_PROGRAM _IQ': ['-99', '-99', '-99'], '004.INITIALIZE_DUT _IQ': ['-99', '-99', '-99'], '026.RX_VERIFY_PER 5180 MCS7 HT20 _PER': ['0', '0.00', ' 10.00'], '012.TX_VERIFY_EVM 2472 MCS7 HT20 _POWER': ['11.00', '15.45', ' 18.00'], '020.TX_VERIFY_EVM 5825 MCS7 HT20 _POWER': ['9', '12.55', ' 16.00']}
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
        tempNum = '%03d'%x
        for key in dataDict.keys():            
            if tempNum in key:
                dataElement = doc.createElement('DataElement')
                dataElement.setAttribute('key', key)
                dataElement.appendChild(doc.createTextNode(dataDict[key][1]))
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