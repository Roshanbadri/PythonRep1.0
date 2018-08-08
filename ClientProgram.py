# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:28:22 2018

@author: Roshan Badrinarayanan
"""

import socket
#Create a socket object for the client
s=socket.socket()
#Connect to the listening server port numbner
s.connect(('10.208.170.178',8080))
#send a message to the server
s.send("Test Client Connection")
#print the message received back from the server
print s.recv(8080)
s.close()