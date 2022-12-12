# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:05:26 2022

@author: Santosh Parse
@program name: Write a program for Linear seperation
"""
import numpy as np
import matplotlib.pyplot as plt
def create_distance_function(a, b, c):
    def distance(x,y):
        nom = a *x + b * y + c
        if nom == 0:
            pos = 0
        elif(nom < 0 and b < 0) or (nom > 0 and b > 0):
            pos = -1
        else:
            pos = 1
        return (np.absolute(nom) / np.sqrt(a**2 + b**2), pos)
    return distance

points = [(3.5,1.8), (1.1,3.9)]
fig, ax = plt.subplots()
ax.set_xlabel("swertness")
ax.set_ylabel("sourness")
ax.set_xlim([-1, 6])
ax.set_ylim([-1, 8])
X=np.arange(-0.5,5,0.1)
index = 10
for (index, (x,y)) in enumerate(points):
    ax.plot(x, y, '*', color="darkorange")
    
step = 0.05

for x in np.arange(0, 1+step, step):
    slope = np.tan(np.arccos(x))
    dist4line1 = create_distance_function(slope, -1, 0)
    
    Y = slope * X
    results = []
    for point in points:
        results.append(dist4line1(*point))

    if results[0][1] != results[1][1]:
        ax.plot(X, Y, 'g-')
    else:
        ax.plot(X, Y, 'r-')
        
plt.show()