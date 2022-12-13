# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:22:59 2022

@author: Santosh Parse
@program name: Write a program to implement Hebb's rule

----------- OUTPUT ----------

First input wuth target = 1
New wt = [0 1 0 0 0 0 0 0 0]
Bias value = 1
Second input with target = -1
Bias value =  0
"""

import numpy as np
x1 = np.array([1,1,1,-1,1,-1,1,1,1])
x2 = np.array([1,1,1,1,-1,1,1,1,1])
b = 0
y = np.array([1,-1])
wtold = np.zeros((9,))
wtnew = np.zeros((9,))

wtnew = wtnew.astype(int)
wtold = wtold.astype(int)

bias = 0
print("First input wuth target = 1")
for i in range(0,9):
    wtold[1] = wtold[i] + x1[i] * y[0]

wtnew = wtold
b= b + y[0]
print("New wt =", wtnew)
print("Bias value =", b)

print("Second input with target = -1")
for i in range(0,9):
    wtnew[i] = wtold[i] + x2[i] * y[1]
b= b + y[1]
print("Bias value = ",b)