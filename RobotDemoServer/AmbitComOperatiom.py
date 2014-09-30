'''
2014/09/30
need pyserial package. version: pyserial 2.7
webSite:https://pypi.python.org/pypi/pyserial
'''

#coding = utf-8

import serial
import io
import time


AMBIT_COM = "COM2"  #ambit serial port name
Robot_SN = "1234567"

'''
@function SFIS serial port 
@param  ComName the SFIS serial port
'''

def SfisComThread(ComName):
    #initialize serial port
    COM = serial.Serial(ComName,9600)
    if not COM.isOpen():
        print('open error')
    writeSnToSfis(COM, Robot_SN, 10)
         

def writeSnToSfis(ser, sn, timeout):
    sfisRtnMsg = ""
    #write data to SFIS serial port
    ser.write(sn.join('\r\n').encode('utf-8'))
    iTime = 0
    #wait the SFIS system response
    while True:
        iTime += 0.1
        #read the serial data(from SFIS serial)
        s += COM.read(COM.inWaiting()).decode('utf-8')
        print(s) 
        if "PASS" in s :
            sfisRtnMsg += s
            break
        else:
            #sleep 0.1 seconds
            time.sleep(0.1)    
        if iTime > timeout:
            sfisRtnMsg += "Sfis response timeout"
    return  sfisRtnMsg        
            

    
if __name__ == '__main__':
    SfisComThread(AMBIT_COM)
    #print(Robot_SN)