# Program Name - Calculate the output of neural net using binary and bipolar sigmoidal function
# Programmer Name - Santosh Parse
#-----------------OUTPUT-----------------------
# Enter number of elements : 3
# Enter the inputs
# 0.5
# 0.2
# 0.3
# [0.5, 0.2, 0.3]
# Enter the weights
# 0.0567
# 0.3344 
# 0.7896
# [0.0567, 0.3344, 0.7896]
# The net input can be calculate as Yin = x1w1 + x2w2 + x3w3
# 0.332
n = int(input("Enter number of elements : "))
print("Enter the inputs")
inputs = []
for i in range(0,n):
    ele = float(input())
    inputs.append(ele)
print(inputs)
print("Enter the weights")
weights = []
for i in range(0,n):
    ele = float(input())
    weights.append(ele)
print(weights)
print("The net input can be calculate as Yin = x1w1 + x2w2 + x3w3")
Yin = []
for i in range(0,n):
    Yin.append(inputs[i] * weights[i])
print(round(sum(Yin), 3))