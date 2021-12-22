# -*- coding: utf-8 -*-

import socket, datetime, csv, threading

class ClientThreading(threading.Thread):
	def __init__(self,addr,conn,port):
		threading.Thread.__init__(self)
		self.conn = conn
		self.addr = addr
		self.port = port

code = "200 OK"
PORT = 8080
listen = 5
data_size = 8192
sock = socket.socket()
sock.bind(('', PORT))
print("Using port "+str(PORT))
sock.listen(listen)
conn, addr = sock.accept()
print("Connection", addr)
newthread = ClientThreading(addr, conn, PORT)
newthread.start()
 

data = conn.recv(data_size)
msg = data.decode()
print(msg)
try:
    file_name = msg[msg.index("GET")+3:msg.index("HTTP")-1]
    print(file_name)
    print(file_name[file_name.index(".")+1:])
    if file_name[file_name.index(".")+1:] != "html" and file_name[file_name.index(".")+1:] != "css" and file_name[file_name.index(".")+1:] != "js" and file_name[file_name.index(".")+1:] != "png" and file_name[file_name.index(".")+1:] != "ico":
        flag = False
    else:
        flag = True
except:
    print("request recieved")
    file_name = "/index.html" 
    flag = True 
if flag:
    try:
        to_open = "/home/boca/web"+file_name
        f = open(to_open, "r")
        msg_new = f.read()
    except:
        code = "404 NOT FOUND"
else:
    code = "403 FORBIDDEN"
    
date = datetime.datetime.today()
print(date)
if "404" in code:
    msg = "Hello!"
    resp = """HTTP/1.1 """+code+"""
Date: """+str(date)+"""
Content-type: text/html
Server: SelfMadeServer v0.0.1
Content-length: 0
Connection: Close
404 FILE NOT FOUND"""
    
elif "403" in code:
    resp = """HTTP/1.1 """+code+"""
Date: """+str(date)+"""
Content-type: text/html
Server: SelfMadeServer v0.0.1
Content-length:"""+str(len("403 FORBIDDEN"))+"""
Connection: Close 
403 FORBIDDEN"""
else:
    resp = """HTTP/1.1 """+code+"""
Date: """+str(date)+"""
Content-type: text/html
Server: SelfMadeServer v0.0.1
Connection: keep-alive
"""+str(msg_new)
conn.send(resp.encode())
print(resp) 
conn.close()
