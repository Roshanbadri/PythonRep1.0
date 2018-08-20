# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:02:12 2018

@author: RO389222
"""

import slash
from can import Message
@slash.fixture
def message():
    m1=Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x66])
    return m1
@slash.fixture(scope='session')
def print1():
    print "Test 2nd fixture"