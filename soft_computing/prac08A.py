"""
Created on Sun Dec 11 22:18

@author: Santosh Parse
@program name: Implement Membership and Identity Operators | in, not in.
"""
def overlapping(list1, list2):
    c=0
    d=0
    for i in list1:
        c+=1
    for i in list2:
        d+=1
    for i in range (0,c):
            for j in range(0,d):
                if(list1[i]==list2[j]):
                    return 1
    return 0

list1=[1,2,3,4,5]
list2=[4,6,7,8,9]
list3=[6,7,8,9,10]
if(overlapping(list1,list2)):
    print("overlapping")
else:
    print("not overlapping")
if(overlapping(list1,list3)):
    print("overlapping")
else:
    print("not overlapping")