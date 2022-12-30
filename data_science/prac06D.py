"""
Created on Fri Dec 30

@author: Santosh Parse
@program name: Organize - Secure Vault Style
"""
import sys
import os
import pandas as pd
import sqlite3 as sq

if sys.platform == 'linux':
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('#'*65) 
print("Working Base: ", Base, 'using', sys.platform)

Company = '01-Vermeulen'
sDataWareHouseDir = Base + '/99-DW'
if not os.path.exists(sDataWareHouseDir):
    os.makedirs(sDataWareHouseDir)
sDatabaseName1 = sDataWareHouseDir + '/datawarehouse.db'
conn1 = sq.connect(sDatabaseName1)

sDatabaseName2 = sDataWareHouseDir + '/datamart.db'
conn2 = sq.connect(sDatabaseName2)

# Load complete BMI data
print('#'*65) 
sTable = 'Dim-BMI'
print('Loading:',sDatabaseName1,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)
print('#'*65) 

# Load Secure data from dataset
sTable = 'Dim-BMI'
print('Loading:', sDatabaseName1, 'Table:', sTable)
sSQL = "SELECT Height, Weight, Indicator,"
sSQL = sSQL + " CASE Indicator When 1 Then 'Pip' When 2 Then 'Norman' When 3 Then 'Grant'"
sSQL = sSQL + " ELSE 'Sam'"
sSQL = sSQL + " END As Name"
sSQL = sSQL + " FROM [Dim-BMI]"
sSQL = sSQL + " WHERE Indicator > 2"
sSQL = sSQL + " ORDER By Height, Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)
DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)

# Storing Secure data to datamart
sTable = 'Dim-BMI-Secure'
print('#'*65)
print('Storing :',sDatabaseName2,'Table:',sTable)
print('#'*65)
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")

# Loading Sam view of BMI from datamart
sTable = 'Dim-BMI-Secure'
print('Loading :',sDatabaseName2,'Table:',sTable)
print('#'*65)
sSQL="SELECT * FROM [Dim-BMI-Secure] WHERE Name = 'Sam';"
PersonFrame2=pd.read_sql_query(sSQL, conn2)

print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('#'*65)
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])
print('#'*65)
print('Only Sam Data')
print(PersonFrame2.head())
