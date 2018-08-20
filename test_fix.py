# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:17:18 2018

@author: RO389222
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 11:32:06 2018

@author: RO389222
"""

import slash
from can import Message

class test_can(slash.Test):
    def before(self):
        print "precond"
        
    @slash.tag('TestName','test_data')
    def test_data(self,message,print1):
        try:
            m1=message
            if m1.data=='deadbeef':
                pass
            else:
                slash.add_failure("failed")

        except Exception as e:
            slash.add_error(e)
    @slash.tag('TestName','test_dlc')
    def test_dlc(self,print1):
        try:
            self.m1=Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x65])
            if self.m1.dlc==8:
                pass
            else:
                slash.add_failure("failed")
        except Exception as e:
            slash.add_error(e)
    def after(self):
        print "postcond"
            
            #raise e
        
    