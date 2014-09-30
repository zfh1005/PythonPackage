from socket import *
import time

RobotScanSN = ''

HOST = ''   
PORT = 6000 #socket port
BUFSIZE = 1024  #read buffer lenght
ADDR = (HOST, PORT)

def RobotServerSocket():
    #init a socket
    tcpSevSock = socket(AF_INET, SOCK_STREAM)
    tcpSevSock.bind(ADDR)
    tcpSevSock.listen(5)
    
    while True:
        #accept clinet socket connect request
        tcpCliSock, addr = tcpSevSock.accept()
        print("connect from:", addr)
        i = 0
        while True:
            i += 1
            #receive the data send from clinet socket
            recvData = tcpCliSock.recv(BUFSIZE).decode()
            sendData = ''
            #print(recvData)
            if 'ASK' in recvData:
                if i % 5 == 0:
                    sendData += 'PASS\r\n'
                elif i %5 == 1:
                    sendData += 'FAIL\r\n'
                elif i %5 == 2:
                    sendData += 'RUN\r\n' 
                elif i %5 == 3:
                    sendData += 'IDLE\r\n' 
                else :
                    sendData += 'ERROR\r\n'                
            elif 'GETOK' in recvData:
                sendData += 'IDLE\r\n'
            elif ':START' in recvData:
                #parse Data SN data from robot scanner
                RobotScanSN = parserRobotSN(recvData)
                sendData += 'RUN\r\n'
            elif 'QUIT' in recvData:    
                break
            else:
                time.sleep(0.1) 
            #send data to clinet socket 
            tcpCliSock.send(sendData.encode())
        tcpCliSock.close()
    tcpSevSock.close()    
    

def parserRobotSN(s):
    #param s format is: SN:START
    return s.split(':')[0] 

if __name__ == '__main__':
    RobotServerSocket()  
   
        