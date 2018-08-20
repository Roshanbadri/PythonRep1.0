# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 11:32:06 2018

@author: RO389222
"""

import slash
from can import Message

class test_can(slash.Test):
    @slash.parametrize('x',[1,2,3])
    @slash.exclude('x',[3])
    @slash.tag('TestName','test_data')
    def test_data(self,x):
        try:
            if x==1:
                self.m1=Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x65])
                if self.m1.data=='deadbeef':
                    pass
                else:
                    slash.add_failure("failed")
            if x==2:
                self.m1=Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x66])
                if self.m1.data=='deadbeef':
                    pass
                else:
                    slash.add_failure("failed")
            if x==3:
               m1=Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x66])
               if self.m1.data=='deadbeef':
                   pass
               else:
                   slash.add_failure("failed")
        except Exception as e:
            slash.add_error(e)
    @slash.tag('TestName','test_dlc')
    def test_dlc(self):
        try:
            self.m1=Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x65])
            if self.m1.dlc==8:
                pass
            else:
                slash.add_failure("failed")
        except Exception as e:
            slash.add_error(e)
            
            #raise e
        
    