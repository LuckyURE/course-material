# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:38:13 2014

@author: joshua_andrews
"""
from itertools import permutations

myChars = 'abcdefghijklmnopqrstuvwxyz'
myList = list(myChars)

myResults = permutations(myList, r=2)

for result in myResults:
    print(result[0] + result[1])
