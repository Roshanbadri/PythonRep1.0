# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:52:00 2018

@author: RO389222
"""

import slash

SUPPORTED_SIZES = [10, 15, 20, 25]
@slash.parametrize('size', SUPPORTED_SIZES)

@slash.tag('All')
def test_size(size):
    assert size==10
@slash.parametrize('size', SUPPORTED_SIZES)
@slash.exclude('size',[15,20,25])
@slash.tag('few')
def test_size1(size):
    assert size==10
    #slash.logger.debug()        
    