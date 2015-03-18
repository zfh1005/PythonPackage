#encoding: UTF-8

#!/usr/bin/env python

import os
import sys
import string
import re
import traceback


LOG_PATH = r'd:\result.txt'
IQ_TEST_RESULT_FILE_NAME = r'SLX3ERG_2015-02-16-13-17-54_EV04.txt'
FAILED_KEY_WORD = r'* F A I L E D *'
PASSED_KEY_WORD = r'* P A S S E D *'

#parse IQ test data
#the param sourcePathath is filePath need parse
def parseIQTestData(sourcePath, iResult):
    #test result is 'PASS'
    if iResult == 2 :
        print('Test result is pass')
    #test result is 'FAIL'
    elif iResult == 3 :
        print('IQ test value failed')
    #IQ API function return error
    elif iResult >= 90 :
        print('IQ API function return error')
        
    #record the test failed information
    ErrorInfo = []
    #record the test items and test data
    resultDict = {}
    
    testResult = 'PASSED'
    
    # Mark the test log's first line is start with 'Testing start ...'
    #if not start 'Testing start ...', close the IQ test process.
    logNormal = False
    
    try:
        #record the temp parser value
        value = []
        tempKey = ' '
        tempValue = ' '
        tempLowerSpec = ' '
        tempUpperSpec = ' '
    
        f = open(sourcePath, 'r')
        lines = f.readlines()

        #show test raw data
        for line in lines:
            print(line)
            
        tempKey1 = ''
        iItemNumber = 0
        IsThereErrorInfo = False
        for line in lines:
            #parse IQ test items
            if (r'_VERIFY_' in line):
                tempKey1 = line.strip()
            #parse EVM value and SPEC
            elif r'EVM_AVG_1' in line:
                iItemNumber += 1
                tempKey2 = tempKey1 + r' _EVM'
                tempValue = line.strip().split(':')[-1].split('dB')[0].strip()
                tempKey = tempKey2
                if r'Failed' in line:
                    testResult = 'FAILED'            
            #parse FREQ value and SPEC
            elif(r'FREQ_ERROR_AVG    ' in line):
                iItemNumber += 1
                tempKey2 = tempKey1 + r' _FREQ'
                tempValue = line.strip().split(':')[-1].split('ppm')[0].strip()
                tempKey = tempKey2
                if r'Failed' in line:
                    testResult = 'FAILED'        
            #parse POWER value and SPEC
            elif(r'POWER_AVG_1    ' in line):
                iItemNumber += 1
                tempKey2 = tempKey1 + r' _POWER'
                tempValue = line.strip().split(':')[-1].split('dBm')[0].strip()
                tempKey = tempKey2
                if r'Failed' in line:
                    testResult = 'FAILED'            
            #parse PER value and SPEC
            elif(r'PER   ' in line):
                iItemNumber += 1
                tempKey2 = tempKey1 + r' _PER'
                tempValue = line.strip().split(':')[-1].split('%')[0].strip()
                tempKey = tempKey2
                if r'Failed' in line:
                    testResult = 'FAILED'
            elif FAILED_KEY_WORD in line:            
                testResult = 'FAILED'
            elif PASSED_KEY_WORD in line:
                testResult = 'PASSED'
            else:
                pass
            
            #insert test item and test data into list 
            #if the key is not empty, record the data
            #print(tempKey)
            if (r'_VERIFY_' in tempKey):
                if tempKey2 not in value:
                    value.append(tempKey)
                    value.append(tempValue)
            #print(value)    
            #get error items and test data
                    
            if IsThereErrorInfo == False:            
                if testResult == 'FAILED':
                    IsThereErrorInfo = True
                    tempKey1 = '%03s%s'%(tempKey.split('.')[0], ('.' + tempKey.split('.')[-1]))
                    ErrorInfo.append(tempKey)
                    ErrorInfo.append(tempValue)
                    break
        f.close()       
        #print(ErrorInfo)
        #print(value)

        if 'Testing start ...' in lines[1]:
            logNormal = True
        else:
            testResult = 'FAILED'
            ErrorInfo = ['888.IQ test error _EX01', '-888']
       
        #insert test result into resultDict
        for x in range(0, len(value), 2):
            tempKey = '%03d.'%(x / 2 + 1 ) + value[x]
            resultDict[tempKey] = [value[x + 1]]
        #print(resultDict)

        if r'FAILED' == testResult:
            if (len(resultDict) <= 0) or (len(ErrorInfo) <= 0):
                resultDict = {'000.test item no value': ['-999']}
                ErrorInfo = ['000.test item no value _EX01', '-999']   
            
    except:
        traceback.print_exc()
        resultDict = {'999.Parser test log file': ['-999']}
        ErrorInfo = ['999.Parser test log file _EX01', '-999']
        testResult = 'FAILED'
        logNormal = False        

    finally:
        print(resultDict, ErrorInfo, testResult, logNormal)
        return resultDict, ErrorInfo, testResult, logNormal

if __name__ == "__main__":
    parseIQTestData(IQ_TEST_RESULT_FILE_NAME, 3)
       
       
    
