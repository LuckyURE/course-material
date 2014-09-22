# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:34:07 2014

@author: joshua_andrews
"""

from sys import argv

if len(argv) < 2:
    print('usage: python3 solution.py OP1 OP2')
else:
    print(int(argv[1]) - int(argv[2]))
