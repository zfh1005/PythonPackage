#encoding: UTF-8
'''
Run IQ test file and parser the test data
'''
import os
import sys
import time
import win32api
import win32gui
import win32con

from WiFiDataParse import parseIQTestData
from ParseWiFiErrorCode import getErrorInfo
from xmlOperation import generateTestReport

from MyConfigParser import readIniFileValue, writeIniFileValue

IQ_TEST_FINISHED_FILE_NAME = r'TestStartUp.ini'
IQ_TEST_RESULT_FILE_NAME = r'.\log\log_all.txt'
IQ_TEST_REPORT_FILE_NAME = r'd:\result.xml'


def IQTestFlow():
    startTime = time.time()
    print('Start test time: ' + time.strftime('%Y/%m/%d %H:%M:%S'))
    #delete result file
    if os.path.exists(IQ_TEST_RESULT_FILE_NAME):
        os.remove(IQ_TEST_RESULT_FILE_NAME)
    #Run IQ test and wait result
    #start IQ test
    writeIniFileValue(IQ_TEST_FINISHED_FILE_NAME, 'TESTER_CONTROL', 'CTRL_MODE', "0")    
    
    #wait 'IQDemo.exe' test finished    
    iTime = 0
    IQTestResult = -1
    while True:
        iTime += 1
        IQTestResult = readIniFileValue(IQ_TEST_FINISHED_FILE_NAME, 'TESTER_CONTROL', 'CTRL_MODE')        
        if (int(IQTestResult) != 0) and (int(IQTestResult) != -1):
            print('IQ_Demo test finished!')
            break        
        else:
            time.sleep(0.1)
            #print('Wait test finished!')
        #110 second(1100) is the timeout time
        if iTime > 1100:            
            break
        
    #parser test result
        
    testDataDict = {}
    errorInfos = []
    if iTime > 1100:
        testDataDict = {'555.Test time': ['110']}
        errorInfos = getErrorInfo(['555.Test time too long _TT00', '-555'])
        print('Test time too long!')
        
    else:
        testDataDict, ErrorInfo, testResult, logNormal = parseIQTestData(IQ_TEST_RESULT_FILE_NAME, int(IQTestResult))
        
        if logNormal == False:
            print('Test log error!')
            
        #report the result
        
        if len(ErrorInfo) != 0:
            errorInfos = getErrorInfo(ErrorInfo)
        else:
            if testResult != 'PASSED':
                errorInfos = getErrorInfo(['666.Parse Failed value error _EX01', '-666'])  
      
    xmlReport = generateTestReport(testDataDict, errorInfos)
    print(xmlReport)

    writeXmlFile(xmlReport)
    print('Finished test time: ' + time.strftime('%Y/%m/%d %H:%M:%S'))
    print('Test time: %0.2f'%(time.time() - startTime))

def writeXmlFile(e):
    f = open(IQ_TEST_REPORT_FILE_NAME, 'a')
    f.write(str(e))
    f.flush()
    f.close()

def getCurrentPath():
    filePath = sys.path[0]
    if os.path.isdir(filePath):
        return filePath
    elif os.path.isfile(filePath):
        return os.path.dirname(filePath)
    
if __name__ == '__main__':
    IQTestFlow()
