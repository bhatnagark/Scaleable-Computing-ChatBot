#Python Server for multiple clients

import socket,sys,os
from threading as Thread
from threading import Lock
import random

threadLock = Lock()

roomList = []


#defining chat message 
def check_msg(msg):
	print('Checking')
	
    if (msg.find('JOIN_CHATROOM'.encode('utf-8'))+1):
		return(1)	
	elif (msg.find('LEAVE_CHATROOM'.encode('utf-8'))+1):
		return(2)
	elif (msg.find('DISCONNECT'.encode('utf-8'))+1):
		return(3)
	elif (msg.find('CHAT:'.encode('utf-8'))+1):
		return(4)	
	elif (msg.find('Kill_Service'.encode('utf-8'))+1):
        return(5)
    else:
		return(6)
    
#Join function

def join(conn_msg,csock):
	#print('Joiner')
	gname = conn_msg.find('Joining_chatroom:'.encode('utf-8'))+17
	gname_end = conn_msg.find('\n'.encode('utf-8'))
	groupname = conn_msg[gname:gname_end]
    
    cname = conn_msg.find('CLIENT_NAME'.encode('utf-8'))+13
	cname_end = conn_msg.find(' '.encode('utf-8'),cname)
	clientname = conn_msg[cname:cname_end]
	rID = 0
	
	if (groupname.decode('utf-8')) == 'room1' :
		print('room1')
        g1_clients.append(clThread.socket)
		rID = 1001
	elif groupname == 'room2' :
        print('room-2')
		g2_clients.append(clThread.socket)
		rID = 1002
        
        
	#sending ackowledgement
	response = "JOINED_CHATROOM: ".encode('utf-8') + groupname+ "\n".encode('utf-8')
	response += "SERVER_IP:".encode('utf-8') + host.encode('utf-8') + "\n".encode('utf-8')
	response += "PORT:".encode('utf-8') + str(port).encode('utf-8') + "\n".encode('utf-8')
	response += "ROOM_REF: ".encode('utf-8') + str(rID).encode('utf-8') +'\n'.encode('utf-8')
	response += "JOIN_ID: ".encode('utf-8') + str(clThread.uid).encode('utf-8') + "\n.encode('utf-8)"  
    csock.send(response)
	grpmessage = "CHAT:".encode('utf-8') + str(rID).encode('utf-8') + "\n".encode('utf-8')
	grpmessage += "CLIENT_NAME:".encode('utf-8') + clientname + "\n".encode('utf-8') 
	grpmessage += "MESSAGE:".encode('utf-8') + clientname + "\n".encode('utf-8') 
	grpmessage += "CLIENT_ID:".encode('utf-8') + str(clThread.uid).encode('utf-8') +"\n".encode('utf-8')
	grpmessage += "JOINED_GROUP".encode('utf-8') +"\n".encode('utf-8')
	if (groupname.decode('utf-8')) == 'room1':
		for x in range(len(g1_clients)):
			g1_clients[x].send(grpmessage)
	elif (groupname.decode('utf-8')) == 'room2':
		for x in range(len(g2_clients)):
			g2_clients[x].send(grpmessage)
	threadLock.release()
    
    return groupname,clientname  


# leaving the chat room            

def leave(conn_msg,csock):
    print('leaving chat room')
	grp_start = conn_msg.find('LEAVING_CHATROOM:'.encode('utf-8')) + 17
	grp_end = conn_msg.find('\n'.encode('utf-8'), grp_start) 

	group_name = conn_msg[grp_start:grp_end]

	response = "LEFT_CHATROOM".encode('utf-8') + groupname + "\n".encode('utf-8')
	response += "JOIN_ID".encode('utf-8') + str(clThread.uid).encode('utf-8')
    
    #sending message to the group
    
	grpmessage = "CLIENT_NAME:".encode('utf-8') + (clThread.clientname).encode('utf-8') + "\n".encode('utf-8')
	grpmessage += "CLIENT_ID:".encode('utf-8') + str(clThread.uid).encode('utf-8') +"\n".encode('utf-8')
	grpmessage += "LEFT GROUP".encode('utf-8')
	print(group_name)
    if(group_name.decode('utf-8')) == 'room1':
		i=g1_clients.index(clThread.socket)
		del g1_clients[i]
	elif(group_name.decode('utf-8')) == 'room2':
		i=g2_clients.index(clThread.socket)
        g2_clients.remove(self.clientname)
        del g2_clients[i]
		csock.send(response)            

    
     
#Chat function
def chat(conn_msg,csock):
	chat_msg_start = conn_msg.find('Mesage:'.encode('utf-8')) + 9
	chat_msg_end = conn_msg.find('\n\n'.encode('utf-8'),chat_msg_start) 

	chat_msg = conn_msg[chat_msg_start:chat_msg_end]

	grp_start = conn_msg.find('CHAT:'.encode('utf-8')) + 6 
	grp_end = conn_msg.find('\n'.encode('utf-8'), grp_start)

	group_name = conn_msg[grp_start:grp_end]
	
	chat_text = 'CHAT: '.encode('utf-8') + str(clThread.roomID).encode('utf-8') + '\n'.encode('utf-8')
	chat_text += 'CLIENT_NAME: '.encode('utf-8') +str(clThread.clientname.encode('utf-8')) + '\n'.encode('utf-8')
	chat_text += 'MESSAGE: ' + chat_msg.encode('utf-8')
	if (group_name.decode('utf-8')) == 'g1':
		for x in range(len(g1_clients)):
			g1_clients[x].send(chat_text)
	elif group_name == 'g2':
		for x in g2_clients:
			g2_clients[x].send(chat_text)


        

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
            print('Connection message')
            print(conn_msg)
			cflag = check_msg(conn_msg)
			print('Connected')
			if cflag == 1 :
				print('joining')
				self.roomname,self.clientname,self.roomID = join(conn_msg,csock)
			elif cflag == 2 : leave(conn_msg,csock)
			elif cflag == 3 : return(0)
			elif cflag == 4 : chat(conn_msg,csock)
			else : print('Error code.wait for more')					
			#print(self.clientname)
			self.chatroom.append(self.roomname)
			print('Total in group 1:')
            print(len(g1_clients))
            print('total clients in group 2 :')
			print(len(g2_clients))
            
            
            
            
            def run(self):
                
		        while True:
			        conn_msg = csock.recv(1024)
			  print('CM')
			print(conn_msg)
			cflag = check_msg(conn_msg)
			if cflag == 1 :
				 self.roomname,self.clientname,self.roomID = join(conn_msg,csock)
			elif cflag == 2 : leave(conn_msg,csock)
			elif cflag == 3 : return(0)
			elif cflag == 4 : chat(conn_msg,csock)
			else : print('Error code. Wait for more')
			self.chatroom.append(self.roomname)
			print('Total clients in group g1: ')
			print(len(g1_clients))
			print('Total clients in group g2: ')
			print(len(g2_clients))


    
def resp(msg,socket):
    msg_start= msg.find('Hello:'.encode('utf-8'))+6
    msg_end = msg.find('\n'.encode('utf-8'),msg_start)

	chat_msg = msg[msg_start:msg_end]

	response = "Hello: ".encode('utf-8') + chat_msg + "\n".encode('utf-8')
	response += "IP: ".encode('utf-8') + str(clThread.ip).encode('utf-8') + "\n".encode('utf-8')
	response += "PORT: ".encode('utf-8') + str(clThread.port).encode('utf-8') + "\n".encode('utf-8')
	response += "StudentID: ".encode('utf-8') + "17307932".encode('utf-8') + "\n".encode('utf-8')


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = int(sys.argv[1])
server.bind((host,port))
print(host)
thread_count = [] 

g1_clients = []
g2_clients = []


while True:
	server.listen(5)
	(csock,(ip,port)) = server.accept()

	print("Connected to ",port,ip)
	
    #monitoring connections
     clThread = client_threads(ip,port,csock)
	clThread.start()
	thread_count.append(clThread)
	print("Threads :")
	print(thread_count)
	print(g1_clients)