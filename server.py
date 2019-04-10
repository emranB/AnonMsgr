import socket,  sys
from threading import Thread 
from socketserver import * 



TCP_IP = '0.0.0.0' 
TCP_PORT = 1111 
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 



'''
Client threads
'''
class ClientThread(Thread): 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print ("[+] New server socket thread started for " , ip , " : ", str(port))
 
    def run(self): # This function is run whenever the ".start()" member is called in Thread
        while True : 
            data = conn.recv(10240).decode('utf-8')
            print ("Server received data:", data)

            input("enter")
            break

            if data == '':
                print ("Client disconnected.\n\nWaiting for client connections...\n\n")
                break

            MESSAGE = input("Server response: ")
            if MESSAGE == 'exit':
                sys.exit(0)
                break
            conn.send(MESSAGE.encode('utf-8'))  # echo 


tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(4) 
    print (" Waiting for clients to connect..." )
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
'''
Finishing all threads
'''
for t in threads: 
    t.join() 

