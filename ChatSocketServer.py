# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:54:47 2018

@author: RO389222
"""
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import random
response=['Hi','Hey there','Hello','Yo','ssup']
greet_key=['Hi','hi','Hey','Hello','hey']
test_key=['test','Testing','testing','Test']
test_response=['You can test this','or test me!','or my patience']
bye=('Bye','bye','cya',)
j=0
memory=[]
resp=''
def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def check_greeting(sentence):
    global response;global greet_key;global test_key;global test_response
    global bye
    global j
    global memory
    global resp

    if sentence.lower() in greet_key:
        return random.choice(response)

    elif sentence in test_key:
        if len(memory)<1:
            resp='You can test this'
            memory.append(('test',resp))
            return resp
        else:
            try:
                for word,resp in memory[j:]:
                    j+=1
                    if resp in test_response:
                        i=test_response.index(resp)
                        del test_response[i]
                        resp=test_response[i]
                        print "resp :-",resp
                        memory.append((sentence,resp))
                        return resp
            except :
                j=0
                i=0
                del memory[0:]
                test_response=['You can test this','Or test me!','Or my patience']
                return "Type anything other than test and I might think of responding"
    elif sentence in bye:
        return "!!Bye"
    else:
        greet_key.append(sentence)
        response.append(sentence)
        return sentence+" back at you"
def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = check_greeting(name)
    client.send(welcome)
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != "{quit}":
            print "Client Says:"+msg
            outmsg=check_greeting(msg)
            print outmsg
            client.send(outmsg)
            if outmsg == "!!Bye":
                client.close()
                del clients[client]
                print "%s has left the chat." % name
                break
        else:
            client.send("{quit}")
            client.close()
            del clients[client]
            print "%s has left the chat." % name
            break


      
clients = {}
addresses = {}

HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()