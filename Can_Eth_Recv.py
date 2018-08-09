import socket
from canethlib import *


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', CANETH_PORT))
    while True:
        datagram, addr = sock.recvfrom(CanEthFrame.MAX_DATAGRAM)
        if datagram:
            print "UDP datagram received from CAN-ETH %s" % addr[0]
            for msg in CanEthFrame(datagram):
                print 'CAN message %07X:' % (msg.id),
                print ' '.join(format(byte, '02X') for byte in msg)

if __name__ == "__main__":
    main()

