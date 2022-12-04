# Program Name - Implement AND/NOT function using McCulloch-Pits neuron (use binary data representation)
# Programmer Name - Santosh Parse
#--------------------OUTPUT--------------------------
# Enter the number of inputs : 2
# For the  2  inputs calculate the net input using Yin = x1w1 = x2w2
# x1 = 1
# x2 = 2
# x1 = 3
# x2 = 5
# x1 =  [1, 3]
# x2 =  [2, 5]
# Yin =  [3, 8]
# After assuming one weight as excitatory and the other as inhibitory Yin =  [-1, -2]
# Y =  [0, 0]
num_ip = int(input("Enter the number of inputs : "))
w1 = 1
w2 = 1
print("For the ", num_ip, " inputs calculate the net input using Yin = x1w1 = x2w2")
x1 = []
x2 = []
for i in range(0, num_ip):
    ele1 = int(input("x1 = "))
    ele2 = int(input("x2 = "))
    x1.append(ele1)
    x2.append(ele2)
print("x1 = ", x1)
print("x2 = ", x2)
n = x1 * w1
m = x2 * w2
Yin = []
for i in range(0, num_ip):
    Yin.append(n[i] + m[i])
print("Yin = ", Yin)
Yin = []
for i in range(0, num_ip):
    Yin.append(n[i] - m[i])
print("After assuming one weight as excitatory and the other as inhibitory Yin = ", Yin)
Y = []
for i in range(0, num_ip):
    if(Yin[i] >= 1):
        ele = 1
        Y.append(ele)
    if(Yin[i] < 1):
        ele = 0
        Y.append(ele)
print("Y = ", Y)