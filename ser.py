import socket
import sys
from thread import *
conn=[0,0]



HOST=''
PORT=12301

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
			break
		conn[1].sendall(reply)
	conn1.close()
def func2(conn2):
	conn2.send('****Welcome to the server****\n(enter q or Q to leave)\n')
	while True:
		data=conn2.recv(1024)
		reply=data
		if not data:
			break
		conn[0].sendall(reply)
	conn2.close()



while 2:
	conn[0], addr =s.accept()
	print 'connected with:' + addr[0] + ':' +str(addr[1])
	start_new_thread(func,(conn[0],))
	conn[1], addr =s.accept()
	print 'connected with:' + addr[0] + ':' +str(addr[1])
	start_new_thread(func2,(conn[1],))
	
s.close()	
	
