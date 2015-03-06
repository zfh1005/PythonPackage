#encoding: UTF-8

#!/usr/bin/env python

from xml.dom import minidom, Node

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
