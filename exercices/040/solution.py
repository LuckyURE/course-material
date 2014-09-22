# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:46:35 2014

@author: joshua_andrews
"""

r = range(0, 100, 1)
lastNum = 0

for num in r:
    if num % 2 == 0:
        num = lastNum + num
        print(num)
        lastNum = num
