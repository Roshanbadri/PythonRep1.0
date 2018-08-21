# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:59:46 2018

@author: RO389222
"""

import can

can.rc['interface'] = 'virtual'

from can import Bus
bus = Bus()

msg1 = can.Message(arbitration_id=0x219, extended_id=False, data=[0, 0, 0, 0, 0, 0, 0, 0])

bus.send(msg1)

m = bus.recv(5)
if m is not None:
    print(m)