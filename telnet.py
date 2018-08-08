
import getpass
import sys
import telnetlib
from SocketServer import ThreadingTCPServer, BaseRequestHandler

HOST = "127.0.0.1,8080"
#user = raw_input("Enter your remote account: ")
#password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
#thread = threading.activeCount()
#tn.read_until("login: ")
#tn.write(user + "\n")
#if password:
 #   tn.read_until("Password: ")
  #  tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()