# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:34:08 2014

@author: joshua_andrews
"""

r = range(0, 1000, 1)

mySum = 0

for num in r:
    if num % 3 == 0 or num % 5 == 0:
        mySum += num

print(mySum)
