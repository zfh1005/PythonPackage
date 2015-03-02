#encoding: UTF-8

#!/usr/bin/env python

import os
import sys
import string
import re
import traceback


LOG_PATH = r'd:\result.txt'
IQ_TEST_RESULT_FILE_NAME = r'4A652A060907.log'
FAILED_KEY_WORD = r'<-Failed'
PASSED_KEY_WORD = r'P A S S'

#parse IQ test data
#the param sourcePathath is filePath need parse
def parseIQTestData(sourcePath):
    #record the test failed information
    ErrorInfo = []
    #record the test items and test data
    resultDict = {}
    #
    testResult = 'PASSED'
    # Mark the test log's first line is start with '=========================Run'
    #if not start '===================Run', close the IQ test process.
    logNormal = False
    
    try:
        #record the temp parser value
        value = []
        tempKey = ' '
        tempValue = ' '
        tempLowerSpec = ' '
        tempUpperSpec = ' '
    
        f = open(sourcePath, 'r', encoding = 'iso-8859-15', errors = 'strict')
        lines = f.readlines()
        for line in lines:
            print(line)
            
        tempKey1 = ''
        IsThereErrorInfo = False
        for line in lines:
            #parse IQ test items
            if (r'_VERIFY_' in line and r' _____' in line):
                tempKey1 = line.strip().split(' _')[0].strip()
            #parse EVM value and SPEC
            elif r'EVM_AVG_1    ' in line: 
                tempKey2 = tempKey1 + r' _EVM'
                tempValue = line.strip().split(':')[-1].split('dB')[0].strip()
                tempLowerSpec = line.strip().split(',')[0].split('(')[-1]
                tempUpperSpec = line.strip().split(',')[-1].split(')')[0]
                if tempLowerSpec == '':
                    tempLowerSpec = '-99'
                tempKey = tempKey2
                if FAILED_KEY_WORD in line:
                    testResult = 'FAILED'
            #parse POWER value and SPEC
            elif(r'POWER_AVG_1    ' in line):
                tempKey2 = tempKey1 + r' _POWER'
                tempValue = line.strip().split(':')[-1].split('dBm')[0].strip()
                tempLowerSpec = line.strip().split(',')[0].split('(')[-1]
                tempUpperSpec = line.strip().split(',')[-1].split(')')[0]
                if tempLowerSpec == '':
                    tempLowerSpec = '0'
                tempKey = tempKey2
                if FAILED_KEY_WORD in line:
                    testResult = 'FAILED'
            #parse FREQ value and SPEC
            elif(r'FREQ_ERROR_AVG    ' in line):
                tempKey2 = tempKey1 + r' _FREQ'
                tempValue = line.strip().split(':')[-1].split('ppm')[0].strip()
                tempLowerSpec = line.strip().split(',')[0].split('(')[-1]
                tempUpperSpec = line.strip().split(',')[-1].split(')')[0]
                if tempLowerSpec == '':
                    tempLowerSpec = '-25'
                if tempUpperSpec == '':
                    tempUpperSpec = '25'    
                tempKey = tempKey2
                if FAILED_KEY_WORD in line:
                    testResult = 'FAILED'        
            #parse MASK value and SPEC
            elif(r'VIOLATION_PERCENT  ' in line):
                tempKey2 = tempKey1 + r' _MASK'
                tempValue = line.strip().split(':')[-1].split('%')[0].strip()
                tempLowerSpec = line.strip().split(',')[0].split('(')[-1]
                tempUpperSpec = line.strip().split(',')[-1].split(')')[0]
                if tempLowerSpec == '':
                    tempLowerSpec = '0'
                if tempUpperSpec == ' ':
                    tempUpperSpec = '99'
                tempKey = tempKey2
                if FAILED_KEY_WORD in line:
                    testResult = 'FAILED'
            #parse PER value and SPEC
            elif((r'PER      ' in line) and (r'_PER' or r'PER_') not in line):
                tempKey2 = tempKey1 + r' _PER'
                tempValue = line.strip().split(':')[-1].split('%')[0].strip()
                tempLowerSpec = line.strip().split(',')[0].split('(')[-1]
                tempUpperSpec = line.strip().split(',')[-1].split(')')[0]
                if tempLowerSpec == '':
                    tempLowerSpec = '0'
                tempKey = tempKey2
                if FAILED_KEY_WORD in line:
                    testResult = 'FAILED'
            #parse another IQ test item
            elif (r'GLOBAL_SETTINGS' in line) and ('_______' in line):            
                tempKey = line.strip().split(' _')[0].strip() + ' _IQ'            
                tempValue = '-99'
                tempLowerSpec = '-99'
                tempUpperSpec = '-99'
            elif (r'CONNECT_IQ_TESTER' in line) and ('_______' in line):
                tempKey = line.strip().split(' _')[0].strip() + ' _IQ'
                tempValue = '-99'
                tempLowerSpec = '-99'
                tempUpperSpec = '-99'
            elif (r'INSERT_DUT' in line) and ('_______' in line):
                tempKey = line.strip().split(' _')[0].strip() + ' _IQ'
                tempValue = '-99'
                tempLowerSpec = '-99'
                tempUpperSpec = '-99'
            elif (r'INITIALIZE_DUT' in line) and ('_______' in line):
                tempKey = line.strip().split(' _')[0].strip() + ' _IQ'
                tempValue = '-99'
                tempLowerSpec = '-99'
                tempUpperSpec = '-99'
            elif (r'LOAD_PATH_LOSS_TABLE' in line) and ('_______' in line): 
                tempKey = line.strip().split(' _')[0].strip() + ' _IQ'
                tempValue = '-99'
                tempLowerSpec = '-99'
                tempUpperSpec = '-99'
            elif (r'DISCONNECT_IQ_TESTER' in line) and ('_______' in line):
                tempKey = line.strip().split(' _')[0].strip() + ' _IQ'
                tempValue = '-99'
                tempLowerSpec = '-99'
                tempUpperSpec = '-99'
            elif (r'REMOVE_DUT' in line) and ('_______' in line):
                tempKey = line.strip().split(' _')[0].strip() + ' _IQ'
                tempValue = '-99'
                tempLowerSpec = '-99'
                tempUpperSpec = '-99'
            elif (r'RUN_EXTERNAL_PROGRAM' in line) and ('_______' in line):
                tempKey = line.strip().split(' _')[0].strip() + ' _IQ'
                tempValue = '-99'
                tempLowerSpec = '-99'
                tempUpperSpec = '-99'
            elif (r'return error' in line):
                tempValue = '-999'
                tempLowerSpec = '-999'
                tempUpperSpec = '-999'
                testResult = 'FAILED'
            elif FAILED_KEY_WORD in line:            
                testResult = 'FAILED'
            else:
                pass
                
            #insert test item and test data into list 
            #if the key is not empty, record the data
            #print(tempKey)
            if (r'_VERIFY_' in tempKey) or ('_IQ' in tempKey):
                if tempKey not in value:
                    value.append(tempKey)
                    value.append(tempLowerSpec)
                    value.append(tempValue)
                    value.append(tempUpperSpec)
            #print(value)    
            #get error items and test data
                    
            if IsThereErrorInfo == False:            
                if testResult == 'FAILED':
                    IsThereErrorInfo = True
                    tempKey1 = '%03d%s'%(int(tempKey.split('.')[0]), ('.' + tempKey.split('.')[-1]))
                    ErrorInfo.append(tempKey1)
                    ErrorInfo.append(tempLowerSpec)
                    ErrorInfo.append(tempValue)
                    ErrorInfo.append(tempUpperSpec)
        f.close()       
        #print(ErrorInfo)

               
        #insert test result into resultDict
        for x in range(0, len(value), 4):
            tempKey = '%03d%s'%((x / 4 + 1), '.' + value[x].split('.')[-1])
            resultDict[tempKey] = [value[x + 1], value[x + 2], value[x + 3]]        
        
        #print(resultDict)
    except:
        traceback.print_exc()
        resultDict = {'999.Parser test log file': ['999', '-999', '999']}
        ErrorInfo = ['999.Parser test log file _EX01', '999', '-999', '999']
        testResult = 'FAILED'
        logNormal = False        

    finally:
        return resultDict, ErrorInfo, testResult, logNormal

if __name__ == "__main__":
    parseIQTestData(IQ_TEST_RESULT_FILE_NAME)
       
       
    
