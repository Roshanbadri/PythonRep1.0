# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:59:17 2018

@author: RO389222
"""
import socket
#initialise a socket object with ethernet TCP as type 'SOCK_STREAM'
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print the socket object details
print sock
#Bind the socket to an unsed port number ex: 8080,8081,1024 etc. 
#the '' parameter shows the server can accept connections from any IP/port
sock.bind(('',8080))
print "Bound to port"
#initiate the socket on 8080 to listen to a max of 5 connections
sock.listen(5)
print "listening"
#get the current system IP: Replace host with the user's system's host name
ip = socket.gethostbyname('D-441006464')
#build a string message to be sent to a target program/system
str="Connected from "+ip
#listen until connections are being made to the server
while True:
    #start accepting connections
    conn,addr = sock.accept()
    #send the message built to the target
    conn.send(str)
    #Receive any messages sent from the target
    data = conn.recv(8080)
    #print the incoming message
    print data
    #print the target's IP/Port
    #print conn,addr
    #close the connection
    conn.close()