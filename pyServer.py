#Python Server for multiple clients

import socket
import threading

#creating socket object 
s=socket.socket()
host=socket.gethostname()
print(host)
port=12221

#defining chat server as threading thread

class ChatServer(threading.Thread):
    #specifyying number of waiting clients
    MAX_WAITING_CONNECTIONS=10
    #Size of the message length
    RECV_BUFFER=4096
    #Placeholder for message length
    RECV_MESG_LEN=10
    
    #Initialize new server
    def init(self,host,port):
        threading.thread.init(self)
        self.host=host
        self.port=port
        self.running= TRUE #whether server should run or not
    
    #binds the multi threaded socket with host and port instead of previous single threaded socket    
    def bind_socket(self):
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, continuos stream of data flow
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # socket option re use the address 
        self.server_socket.bind((self.host, self.port)) # bind the host name and port
        self.server_socket.listen(self.MAX_WAITING_CONNECTIONS) 
        self.connections.append(self.server_socket)
    

#threading required
while 1:
    c,adrs= s.accept()
    print("got connceted from %s", +str(adrs))
    
    response="welcome to the chatroom"
    c.send(response.encode('ascii'))
    c.close()