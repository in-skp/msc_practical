"""
Created on Sun Dec 11 22:18

@author: Santosh Parse
@program name: Implement membership and identity operators is, is not.
"""
details=[]
name=input("Enter you name:")
details.append(name)
age=float(input("Enter your exact age:"))
details.append(age)
roll_no=float(input("Enter your roll no:"))
details.append(roll_no)
for i in details:
    print(i)
    print("Int= ",type(i)is not int)
    print("Float=",type(i) is not float)
    print("String=",type(i) is not str)