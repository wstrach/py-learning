#!/usr/bin/python
#
# SERWER
#

import socket

def server():
proto = socket.getprotobyname('tcp') # [1]
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto)

serv.bind(("localhost", 2222)) # [2]
serv.listen(1) # [3]
return serv

serv = server()

while 1:
conn, addr = serv.accept() # [4]
while 1:
message = conn.recv(64) # [5]
if message:
conn.send('Hi, I am a server, I received: ' + message)
else:
break
conn.close()
