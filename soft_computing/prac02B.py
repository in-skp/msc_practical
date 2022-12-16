# Program Name - Implement XOR funtion using McCulloch-Pits neural net
# Programmer Name - Santosh Parse
#--------------------OUTPUT----------------------------
# Enter weights
# Weight w11 = 1
# Weight w12 = -1
# Weight w21 = -1
# Weight w22 = 1
# Weight v1 = 1
# Weight v2 = -1
# Enter Threshold Value 
# theta = 1
# z1 =  [ 0 -1  1  0]
# z2 =  [ 0  1 -1  0]
# Yin =  [0. 1. 1. 0.]
# Output of Net
# y =  [0 1 1 0]
# z =  [0 1 1 0]
# McCulloch-Pits Net for XOR function
# Weights of Neuron z1
# 1
# -1
# Weights of Neuron z2
# -1
# 1
# Weights of Neuron Y
# 1
# -1
# Threshold value
# 1
import numpy as np
print("Enter weights")
w11 = int(input("Weight w11 = "))
w12 = int(input("Weight w12 = "))
w21 = int(input("Weight w21 = "))
w22 = int(input("Weight w22 = "))
v1 = int(input("Weight v1 = "))
v2 = int(input("Weight v2 = "))
print("Enter Threshold Value ")
theta = int(input("theta = "))
x1 = np.array([0,0,1,1])
x2 = np.array([0,1,0,1])
z = np.array([0,1,1,0])
con = 1
y1 = np.zeros((4,))
y2 = np.zeros((4,))
y = np.zeros((4,))
while con == 1:
    zin1 = np.zeros((4,))
    zin2 = np.zeros((4,))
    zin1 = x1 * w11 + x2 * w12
    zin2 = x1 * w21 + x2 * w22

    print("z1 = ", zin1)
    print("z2 = ", zin2)

    for i in range(0, 4):
        if zin1[i] >= theta:
            y1[i] = 1
        else:
            y1[i] = 0
        if zin2[i] >= theta:
            y2[i] = 1
        else:
            y2[i] = 0
    
    Yin = np.array([])
    Yin = y1 + v1 + y2 + v2
    for i in range(0, 4):
        if Yin[i] >= theta:
            y[i] = 1
        else: 
            y[i] = 0
    print("Yin = ", Yin)
    print("Output of Net")
    y = y.astype(int)
    print("y = ", y)
    print("z = ", z)

    if np.array_equal(y, z):
        con = 0
    else:
        print("Net is not learning, Enter another set of weights and threshold value")
        w11 = int(input("Weight w11 = "))
        w12 = int(input("Weight w12 = "))
        w21 = int(input("Weight w21 = "))
        w22 = int(input("Weight w22 = "))
        v1 = int(input("Weight v1 = "))
        v2 = int(input("Weight v2 = "))
        theta = int(input("theta = "))

print("McCulloch-Pits Net for XOR function")
print("Weights of Neuron z1")
print(w11)
print(w21)
print("Weights of Neuron z2")
print(w12)
print(w22)
print("Weights of Neuron Y")
print(v1)
print(v2)
print("Threshold value")
print(theta)