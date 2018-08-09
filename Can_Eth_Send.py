#!/usr/bin/env python

import socket
from canethlib import *


CANETH_IP   = "10.208.170.178" 

#def main():
msg = CanMsg(0x123, (0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88))
frame = CanEthFrame()
frame.append(msg)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1);
sock.sendto(frame.pack(), (CANETH_IP, CANETH_PORT))
print 'CAN message sent %07X:' % (msg.id),
print ' '.join(format(byte, '02X') for byte in msg)


#if __name__ == "__main__":
 #   main()
