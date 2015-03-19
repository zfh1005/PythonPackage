from WiFiDataParse import parseIQTestData
from ParseWiFiErrorCode import getErrorInfo
from xmlOperation import generateTestReport

IQ_TEST_RESULT_FILE_NAME = r'SM80128_2015-01-03-04-56-10_EV04.txt'

testDataDict, ErrorInfo, testResult, logNormal = parseIQTestData(IQ_TEST_RESULT_FILE_NAME, 3)

errorInfos = []

if len(ErrorInfo) != 0:
    errorInfos = getErrorInfo(ErrorInfo)
else:
    if testResult != 'PASSED':
        errorInfos = getErrorInfo(['666.Parse Failed value error _EX01', '-666'])
xmlReport = generateTestReport(testDataDict, errorInfos)

print(xmlReport)
