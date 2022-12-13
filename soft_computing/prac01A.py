# Program Name - Design a simple linear neural network model
# Programmer Name - Santoh Parse
# ------------------ OUTPUT -----------------------
# Enter the input x = 0.2
# Enter the bias b = 0.1
# Enter the weight w = 0.3
# ****----OUTPUT----****
# net =  0.16
# Output =  0.16
x = float(input("Enter the input x = "))
b = float(input("Enter the bias b = "))
w = float(input("Enter the weight w = "))
net = b + x * w
print("****----OUTPUT----****")
print("net =", net)
if(net < 0):
    out = 0
elif (net >= 0) & (net <= 1):
    out = net
else:
    out = 1
print("Output =", out)