#Python Server for multiple clients

import socket
import threading as Thread
import random

#creating socket object 
s=socket.socket()
host=socket.gethostname()
print(host)
port=12221

#diconnect function
def discon():
	clThread.exit()

#defining chat server as threading thread

class client_threads(Thread):
   
    #Initialize new server
    def __init__(self,ip,port,socket):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.chatroom =[] 
		self.socket = socket
		self.uid = random.randint(1000,2000)
		self.roomname = ''
		self.clientname = ''
   
    #Running
    def run(self):
		while True:
			conn_msg = csock.recv(1024)
			cflag = check_msg(conn_msg)
			print('Connected')
			if cflag == 1 :
				 print('joining')
				 self.roomname,self.clientname = join(conn_msg,csock)
			elif cflag == 2 : leave(conn_msg,csock)
			elif cflag == 3 : discon(csock)
			elif cflag == 4 : chat()
			else : pass					 #error code for incorrect message	
			print(self.clientname)
			self.chatroom.append(self.roomname)
			print('roomnames')
			print(self.chatroom)
    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 10001
server.bind((host,port))
print(host)
thread_count = [] 

g1_clients = []
g2_clients = []


while True:
	server.listen(4)
	(csock,(ip,port)) = server.accept()

	print("Connected to ",port,ip)
	#monitoring connections

	clThread = client_threads(ip,port,csock)
	clThread.start()
	thread_count.append(clThread)
	print("Threads :")
	print(thread_count)
	print(g1_clients)