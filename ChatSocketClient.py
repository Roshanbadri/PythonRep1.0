# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:57:04 2018

@author: RO389222
"""

#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    outmsg=raw_input("Enter Your Message:")
    #client_socket.send(bytes(msg, "utf8"))
    client_socket.send(outmsg)
    if outmsg == "{quit}":
        client_socket.close()
        
        
def receive():
    """Handles receiving of messages."""
    while True:
        try:
            send()
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print "Server Says:"+msg
        except OSError:  # Possibly client has left the chat.
            break
   

HOST = '10.208.170.178'
PORT = 8080
if not PORT:
    PORT = 5000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=receive)
receive_thread.start()
receive_thread.join()
