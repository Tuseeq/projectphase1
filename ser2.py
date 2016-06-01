import socket
import sys
from thread import *
conn=[]
busy=[]
clnt=[]
rqst=[]
i=0
count=0
for a in range(10):
	conn.append(0)
	busy.append(0)
	clnt.append('')
	rqst.append(0)
HOST=''
PORT=5895

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "socket created:"


try:
    s.bind((HOST,PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'binding complete'

s.listen(10)
print 'listening'


################################################
def func(i1,i2):
	conn[i2].sendall('***connected now you can chat:***\n**to leave chat enter: exit***\n')
	while True:
		if busy[i1]==0:
			busy[i1]=0
			busy[i2]=0
			start_new_thread(starts,(conn[i1],i1))
			break
		else:
			data=conn[i1].recv(1024)
			reply=clnt[i1]+':->>> '+ data 
			if data=='goodbye!\n (user left server)':
				busy[i1]=0
				busy[i2]=0
				conn[i2].sendall(data)			
				break
			elif data=='exit':
				busy[i1]=0
				busy[i2]=0
				conn[i2].sendall('user left chat!!\n')
				start_new_thread(starts,(conn[i1],i1))
				break		
			elif conn[i2]!=0:
				conn[i2].sendall(reply)
			
			
	print  addr[0]+ ':' +str(addr[1]) + ' is disconnected' 
	conn[i1].close()
	conn[i1]=0

################################################
def starts(conn1,i2):	
	
	for a in range(count):
		if conn[a]!=0 and a!=i2:
			conn[a].send(str(i2)+': '+clnt[i2]+' connected\n')
	while busy[i2]!=1:	
		w='\nConnected clients:\n'
		conn1.send(w)
	
		for a in range(count):
			if conn[a]!=0:
				if a==i2:
					wx='YOU!\n'
				elif busy[a]==0:
					wx=str(a)+': '+clnt[a]+' status:Available\n'
				elif busy[a]==1:
					wx=str(a)+': '+clnt[a]+' status:busy\n'
				conn1.send(wx)
		conn1.send('Select any available person number:')
		n=conn1.recv(1024)
		if n=='goodbye!\n (user left server)':
			conn1.close()
			conn[i2]=0			
			break
		elif rqst[i2]==0:
			if busy[int(n)]!=0:
				conn1.send('Busy at the moment: try someone else!\n')
			else:
				rqst[int(n)]=1
				busy[i2]=1
				conn[int(n)].sendall('recieved a rqst from '+clnt[i2]+'\n do you want to talk (select number)\n'+str(i2)+' :YES or -1:NO\n')		
		elif rqst[i2]==1:
			if n=='-1':
				rqst[i2]=0
				busy[int(n)]=0
			else:
				rqst[i2]=0
				busy[i2]=1
				print 1
				start_new_thread(func,(int(n),i2))
				print 32
				start_new_thread(func,(i2,int(n)))
				break 





		
while 1:
	conn[i], addr =s.accept()	
	count+=1
	print 'connected with:' + addr[0]+ ':' +str(addr[1])
	w='****Welcome to the server****\nPlease enter your name:'
	conn[i].send(w)
	name=conn[i].recv(1024)			
	clnt[i]=name
	busy[i]=0
	start_new_thread(starts,(conn[i],i))
	i+=1
	#start_new_thread(func,(conn[b],b))
		
s.close()	
	
