# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:36:09 2022

@author: Santosh Parse
@program name: Write a program to implement of delta rule
----------------- OUTPUT -----------------
Inital inputs:1
Inital inputs:1
Inital inputs:1
Inital weights:0.2
Inital weights:0.3
Inital weights:0.4
Desired Output:1
Desired Output:1
Desired Output:1
Enter learning rate:0.5
"""
import numpy as np
import time
np.set_printoptions(precision=2)
x = np.zeros((3,))
weights = np.zeros((3,))
desired = np.zeros((3,))
actual = np.zeros((3,))
for i in range(0,3):
    x[i] = float(input("Inital inputs:"))

for i in range(0,3):
    weights[i] = float(input("Inital weights:"))

for i in range(0,3):
    desired[i] = float(input("Desired Output:"))
    
a = float(input("Enter learning rate:"))

actual = x * weights
print("actual ", actual)
print("desired ", desired)

print("*"*30)

while True:
    if np.array_equal(desired, actual):
        break
    else:
        for i in range(0,3):
            weights[i] = weights[i] + a * (desired[i] - actual[i])
    actual = x * weights
    print("weights ", weights)
    print("actual ", actual)
    print("desired", desired)
            
print("*"*30)
print("Final output")
print("Corrected weights",weights)
print("actual",actual)
print("desired",desired)