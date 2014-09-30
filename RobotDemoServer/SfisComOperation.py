'''
2014/09/30
need pyserial package. version: pyserial 2.7
webSite:https://pypi.python.org/pypi/pyserial
'''

#coding = utf-8

import serial
import io
import time

SFIS_COM = "COM2"   #SFIS system used serial port
SFIS_PN = "U89Z022.10"  #demo SFIS product name

'''
@function SFIS serial port 
@param  ComName the SFIS serial port
'''

def SfisComThread(ComName):
    #initialize SFSI system serial port 
    COM = serial.Serial(ComName,9600)
    if not COM.isOpen():
        print('open error')
    while True:
        #read the serial data(from Ambit serial)
        s = COM.read(COM.inWaiting()).decode('utf-8')
        print(s)  
        if len(s) == 7:
            #response status to Ambit serial 
            COM.write((s + SFIS_PN + "PASS\r\n").encode('utf-8'))
        elif "QUIT" in s :
            COM.close()
        else:
            time.sleep(0.1)    
          
   
if __name__ == '__main__':
    SfisComThread(SFIS_COM)