"""
Created on Sun Dec 11 22:18

@author: Santosh Parse
@program name: Implement membership and identity operators | in, not in.
"""
list1=[]
print("Enter 5 numbers")
for i in range(0,5):
    v=int(input())
    list1.append(v)
list2=[]
print("Enter 5 numbers")
for i in range(0,5):
    v=int(input())
    list2.append(v)
flag=0
for i in list1:
    if i in list2:
        flag=1
if(flag==1):
    print("The lists Overlap")
else:
    print("The lists do not Overlap")