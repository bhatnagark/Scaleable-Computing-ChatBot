import socket 
 
 def join():
 + 
 # create a socket object 
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  
 # get local machine name 
 host = input('Enter Hostname')
  
 port = 10001 
 # connection to hostname on the port. 
 s.connect((host, port))                                
 
 chatroom = input('Enter Chatroom name to enter')
 Cname = input('Give Client Name')
 
 conn_msg = "JOIN_CHATROOM:".encode('utf-8') + chatroom.encode('utf-8')  "\n".encode('utf-8')
 conn_msg += "CLIENT IP: \n".encode('utf-8')
 conn_msg += "PORT: \n".encode('utf-8')
 conn_msg += "CLIENT_NAME:".encode('utf-8') + Cname.encode('utf-8') + "\n".encode('utf-8')
 
 s.send(conn_msg)
 
 while(1):
 	message = s.recv(1024)
 	print('Enter Option to choose:')
 	print('1. Join')
 	print('2. Chat')
 	print('3. Leave')
 	print('4. Disconnect')
 	task = input('')
 	if task == 1:
 		join()
 	elif task == 2:
 		chat()
 	elif task == 3:
 		leave()
 	elif task == 4:
 		discon()
 	elif task == 5:
  	print('Error')