# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:07:07 2018

@author: RO389222
"""

import slash
@slash.fixture
def ip():
    if raw_input("State ON/OFF:")=="ON":
        pass
    return ip
#@slash.nofixtures
def test_target(ip):
    #a=ip()
    assert 1==1