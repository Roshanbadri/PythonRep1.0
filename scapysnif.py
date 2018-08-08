# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:17:51 2018

@author: RO389222
"""

from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#import re

def packet_callback(packet):
    if packet[TCP].payload:
        pkt = str(packet[TCP].payload)
        if packet[IP].dport == 8080:
            print("\n{} ----HTTP----> {}:{}:\n{}".format(packet[IP].src, packet[IP].dst, packet[IP].dport, str(bytes(packet[TCP].payload))))

sniff(filter="tcp", prn=packet_callback, store=0)