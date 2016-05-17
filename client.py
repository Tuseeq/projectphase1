
import socket  
from thread import *   

s = socket.socket()         
HOST = ''
PORT = 12301   
s.connect((HOST,PORT))
p= s.recv(1024)
print p

def clin(d):
	while True:
		a=d.recv(1024)
		print '           ' +a +'  :user'

start_new_thread(clin,(s,))
while 1:
	q=raw_input()
	if q=='q' or q=='Q':
		s.sendall('goodbye!\n (user left server)')
		break
	else:
		s.sendall(q)
s.close()                    
