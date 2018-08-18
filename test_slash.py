# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:11:08 2018

@author: RO389222
"""
import slash
from can import Message

class test_slash(slash.Test):
    #x=['dlc','data']
#@slash.parametrize('param',x)
#@slash.exclude('dlc')
    @slash.parametrize('param',[1,2,3])   
    #@slash.exclude('param',[3])
    @slash.tag('TestName','dat')   
    def test_can(self,param):
        try:
            if param==1:
                self.m1 = Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x66])
                assert self.m1.data == 'deadbeef'
            elif param==2:
                self.m1 = Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x67])
                assert self.m1.data == 'deadbeef'
            elif param==3:
                assert 1==1
        except Exception as e:
            print "Error"
            slash.logger.debug(e)
    @slash.tag('TestName','dlc')
    def test_CAN1(self):
        self.m1 = Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x66])
        assert self.m1.dlc == 8    