import socket 
from threading import Thread
 
def connect():
	chatroom = input('Enter Chatroom name to enter')

	conn_msg = "JOIN_CHATROOM:".encode('utf-8') + chatroom.encode('utf-8') + "\n".encode('utf-8')
	conn_msg += "CLIENT IP: \n".encode('utf-8')
	conn_msg += "PORT: \n".encode('utf-8')
	conn_msg += "CLIENT_NAME:".encode('utf-8') + Cname.encode('utf-8') + "\n".encode('utf-8')
	s.send(conn_msg)
    s.send(conn_msg)
    
def chat():
	croom = input('What roo to chat with')
	chat_message = input('Message')
	msg = "CHAT: ".encode('utf-8') + croom.encode('utf-8') + "\n".encode('utf-8')
	msg += "JOIN_ID: ".encode('utf-8') + str(jID).encode('utf-8') + "\n".encode('utf-8')
	msg += "CLIENT_NAME: ".encode('utf-8') + Cname.encode('utf-8') + "\n".encode('utf-8')
	msg += "MESSAGE: ".encode('utf-8') + chat_message.encode('utf-8') + "\n\n".encode('utf-8')
	s.send(msg)    
 
 
# create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name 
host = input('Enter Hostname')
port = input('Port') 

# connecting with the port

s.connect((host, int(port)))                                
Cname = input('Give Client Name')
join()
jID=0
data = s.recv(1024)
print(data.decode(encoding='utf-8'))
p = data.find(b'JOINED')
if p==0:
	jID_start = data.find('JOIN_ID'.encode('utf-8'))+9
	jID_end = data.find('\n'.encode('utf-8'),jID_start)-1
	jID = str(data[jID_start:jID_end])

serverThread = Client(s)
serverThread.start()

def leave(s):
	rTL = input('Which room to leave')
	msg = "LEAVING_CHATROOM: ".encode('utf-8') + rTL.encode('utf-8') + "\n".encode('utf-8')
	msg += "JOIN_ID: ".encode('utf-8') + jID.encode('utf-8') + "\n".encode('utf-8')
	msg += "CLIENT_NAME: ".encode('utf-8') + Cname.encode('utf-8') 	
	s.send(msg)	

def discon():
	msg = "DISCONNECTING: \n".encode('utf-8') 
	msg += "PORT: \n".encode('utf-8')
	msg += "CLIENT_NAME: ".encode('utf-8') + Cname.encode('utf-8') + "\n".encode('utf-8')
	s.send(msg)
	
	s.close()
	os._exit(1)

while(1):
	print('Enter Option to choose:')
	print('1. Join')
	print('2. Chat')
	print('3. Leave')
	print('4. Disconnect')
	task = input('?')
	if task == '1':
		connect()
	elif task == '2':
		print('Chatting')
		chat(s)
	elif task == '3':
		leave(s)
	elif task == '4':
		discon()
	elif task == '5':
		print('Error')