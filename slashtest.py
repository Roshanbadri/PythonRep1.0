# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:11:08 2018

@author: RO389222
"""

import slash
from can import Message

class test(object):
    #x=['dlc','data']
#@slash.parametrize('param',x)
#@slash.exclude('dlc')
    def __init__(self):
        self.m1=Message()
    @slash.fixture
    def message(self):
        self.m1 = Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x66])
    @slash.tag('TestName','data')
    def test_CAN(self,message):
        assert self.m1.data == 'deadbeef'
    @slash.tag('TestName','dlc')
    def test_CAN1(self,message):
        assert self.m1.dlc == 8    
