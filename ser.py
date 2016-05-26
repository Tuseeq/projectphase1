import socket
import sys
from thread import *
conn=[0,0]
i=0


HOST=''
PORT=5883

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "socket created:"


try:
    s.bind((HOST,PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'binding complete'

s.listen(2)
print 'listening'

###

def func(conn1):
	conn1.send('****Welcome to the server****\n(enter q or Q to leave)\n')
	while True:
		data=conn1.recv(1024)
		reply=data 
		if not data:
			if conn1==conn[1]:
				conn[1]=0
			elif conn1==conn[0]:
				conn[0]=0
			break
		if conn1==conn[1] and conn[0]<>0:
			conn[0].sendall(reply)
		elif conn1==conn[0] and conn[1]<>0 :
			conn[1].sendall(reply)
	conn1.close()




while 1:
	#if conn[i]==0:
		conn[i], addr =s.accept()
		print 'connected with:' + addr[0]+ ':' +str(addr[1])
		start_new_thread(func,(conn[i],))
		if i==0:
			i=i+1
		elif i==1:
			i=i-1	
s.close()	
	
