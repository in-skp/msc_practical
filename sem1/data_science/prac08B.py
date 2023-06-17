"""
Created on Mon Jan 02

@author: Santosh Parse
@program name: Transforming Data - Simple Linear Regression 
"""
import sys
import os
import pandas as pd
import sqlite3 as sq
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

if sys.platform == 'linux':
    Base = os.path.expanduser('~') + 'VKHCG'
else:
    Base = 'C:/VKHCG'
print('#'*65) 
print("Working Base: ", Base, 'using', sys.platform)
print('#'*65) 

Company='01-Vermeulen'
sDataBaseDir=Base + '/' + Company + '/04-Transform/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)

sDatabaseName1=sDataBaseDir + '/Vermeulen.db'
conn1 = sq.connect(sDatabaseName1)
sDataVaultDir=Base + '/88-DV'
if not os.path.exists(sDataVaultDir):
    os.makedirs(sDataVaultDir)

sDatabaseName2=sDataVaultDir + '/datavault.db'
conn2 = sq.connect(sDatabaseName2)
sDataWarehouseDir=Base + '/99-DW'
if not os.path.exists(sDataWarehouseDir):
    os.makedirs(sDataWarehouseDir)

sDatabaseName3=sDataWarehouseDir + '/datawarehouse.db'
conn3 = sq.connect(sDatabaseName3)

t=0
tMax=((300-100)/10)*((300-30)/5)
for heightSelect in range(100,300,10):
    for weightSelect in range(30,300,5):
        height = round(heightSelect/100,3)
        weight = int(weightSelect)
        bmi = weight/(height*height)
        if bmi <= 18.5:
            BMI_Result=1
        elif bmi > 18.5 and bmi < 25:
            BMI_Result=2
        elif bmi > 25 and bmi < 30:
            BMI_Result=3
        elif bmi > 30:
            BMI_Result=4
        else:
            BMI_Result=0
        PersonLine=[('PersonID', [str(t)]),
                  ('Height', [height]),
                  ('Weight', [weight]),
                  ('bmi', [bmi]),
                  ('Indicator', [BMI_Result])]
        t+=1
        # print('Row:',t,'of',tMax)
        if t==1:
            PersonFrame = pd.DataFrame.from_dict(dict(PersonLine))
        else:
            PersonRow = pd.DataFrame.from_dict(dict(PersonLine))
            PersonFrame = pd.concat([PersonFrame, PersonRow])

DimPerson=PersonFrame
DimPersonIndex=DimPerson.set_index(['PersonID'],inplace=False)

sTable = 'Transform-BMI'
print('#'*65)
print('Storing :',sDatabaseName1,'\nTable:',sTable)
print('#'*65)
DimPersonIndex.to_sql(sTable, conn1, if_exists="replace")

sTable = 'Person-Satellite-BMI'
print('#'*65)
print('Storing :',sDatabaseName2,'\nTable:',sTable)
print('#'*65)
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")

sTable = 'Dim-BMI'
print('#'*65)
print('Storing :',sDatabaseName3,'\nTable:',sTable)
print('#'*65)
DimPersonIndex.to_sql(sTable, conn3, if_exists="replace")

fig = plt.figure()
PlotPerson=DimPerson[DimPerson['Indicator']==1]
x=PlotPerson['Height']
y=PlotPerson['Weight']
plt.plot(x, y, ".")
PlotPerson=DimPerson[DimPerson['Indicator']==2]
x=PlotPerson['Height']
y=PlotPerson['Weight']
plt.plot(x, y, "o")
PlotPerson=DimPerson[DimPerson['Indicator']==3]
x=PlotPerson['Height']
y=PlotPerson['Weight']
plt.plot(x, y, "+")
PlotPerson=DimPerson[DimPerson['Indicator']==4]
x=PlotPerson['Height']
y=PlotPerson['Weight']
plt.plot(x, y, "^")
plt.axis('tight')
plt.title("BMI Curve")
plt.xlabel("Height(meters)")
plt.ylabel("Weight(kg)")
plt.plot()

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-50:]
diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-50:]

regr = linear_model.LinearRegression()

regr.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = regr.predict(diabetes_X_test)

print('Coefficients: \n', regr.coef_)
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)
plt.xticks(())
plt.yticks(())
plt.axis('tight')
plt.title("Diabetes")
plt.xlabel("BMI")
plt.ylabel("Age")
plt.show()