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

IQ_BAT_TITLE_NAME = r'ROKU_WIFI'
IQ_BAT_FILE_NAME = r'IQ.bat'
IQ_TEST_FINISHED_FILE_NAME = r'D:\ETH_PT1(U89Z022)\litepoint.tmp'
IQ_TEST_RESULT_FILE_NAME = r'D:\ETH_PT1(U89Z022)\log\log_all.txt'
IQ_TEST_REPORT_FILE_NAME = r'd:\result.xml'


def IQTestFlow():
    startTime = time.time()
    print('Start test time: ' + time.strftime('%Y/%m/%d %H:%M:%S'))
    if not os.path.exists(IQ_TEST_FINISHED_FILE_NAME):
        createFile(IQ_TEST_FINISHED_FILE_NAME)
    if os.path.exists(IQ_TEST_RESULT_FILE_NAME):
        os.remove(IQ_TEST_RESULT_FILE_NAME)
    #Run IQ file and wait result
    #check 'IQRunConsole.exe' running or not?
    hwnd = win32gui.FindWindow('ConsoleWindowClass', IQ_BAT_TITLE_NAME)
    if hwnd < 1:
        #not find the windows, run the 'IQRunConsole.exe'
        #runFileName = getCurrentPath() + IQ_BAT_FILE_NAME
        
        os.startfile(IQ_BAT_FILE_NAME)    
        while True:
            hwnd = win32gui.FindWindow('ConsoleWindowClass', IQ_BAT_TITLE_NAME)
            if hwnd < 1:
                time.sleep(0.01)
            else:
                break
    else:
        #send '\n' into 'IQRunConsole.exe'
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 13, 0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, 13, 0)
    
	#hide the IQConsoleRun test windows    
    win32gui.ShowWindow(hwnd, False)
    
    #wait 'IQRunConsole.exe' test finished    
    iTime = 0
    #finishFileName = getCurrentPath() + IQ_TEST_FINISHED_FILE_NAME
    while True:
        iTime += 1
        if not os.path.exists(IQ_TEST_FINISHED_FILE_NAME):
            time.sleep(1)
            print('IQ bat file test finished!')
            break
        else:
            time.sleep(0.1)
            #print('Wait test finished!')
        if iTime > 1100:            
            break
        
    #parser test result
    #resultFileName = getCurrentPath() + IQ_TEST_RESULT_FILE_NAME
    testDataDict = {}
    errorInfos = []
    if iTime > 1100:
        testDataDict = {'555.Test time': ['0', '110', '110']}
        errorInfos = getErrorInfo(['555.Test time too long _TT00', '555', '-555', '555'])
        print('Test time too long!')
        win32api.SendMessage(hwnd, win32con.WM_CLOSE)
        
    else:
        testDataDict, ErrorInfo, testResult, logNormal = parseIQTestData(IQ_TEST_RESULT_FILE_NAME)
        
        if logNormal == False:
            print('Test log error!')
            win32api.SendMessage(hwnd, win32con.WM_CLOSE)
            
        #report the result
        
        if len(ErrorInfo) != 0:
            errorInfos = getErrorInfo(ErrorInfo)
        else:
            if testResult != 'PASSED':
                errorInfos = getErrorInfo(['666.Parse Failed value error _EX01', '666', '-666', '666'])  
      
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
    
def createFile(e):
    f = open(e, 'a')
    f.write(str('temp'))
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
