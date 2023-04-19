# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:11:15 2022

@author: Santosh Parse
@program name: Write a program for Back Propogation Algorithm
------------- OUTPUT ------------
Enter weights first network:1
Enter base first network:1
Enter weights second network:2
Enter base second network:1
Enter learning coefficient:0.5
The updated weight of first n/w w11 =  1.0103607311020744
The updated weight of second n/w w21 =  1.9740518729157233
The updated base of first n/w b10 =  1.0
The updated base of second n/w b20 =  1.0
"""

import math
a0 = -1
t = -1
w10 = float(input("Enter weights first network:"))
b10 = float(input("Enter base first network:"))
w20 = float(input("Enter weights second network:"))
b20 = float(input("Enter base second network:"))
c = float(input("Enter learning coefficient:"))

n1 = float(w10 * c + b10)
a1 = math.tanh(n1)
n2 = float(w20 * a1 + b20)
a2 = math.tanh(float(n2))
e = t - a2
s2 = -2 * (1 - a2 * a2) * e
s1 = (1 - a1 * a1) * w20 * s2

w21 = w20 - (c * s2 * a1)
w11 = w10 - (c * s1 * a0)
b21 = b20 - (c * s2)
b11 = b10 - (c * s1)

print("The updated weight of first n/w w11 = ", w11)
print("The updated weight of second n/w w21 = ", w21)
print("The updated base of first n/w b10 = ", b10)
print("The updated base of second n/w b20 = ", b20)

