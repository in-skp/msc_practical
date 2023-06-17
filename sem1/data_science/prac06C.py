"""
Created on Fri Dec 30

@author: Santosh Parse
@program name: Organize - Island Style
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

# Loading Island of BMI
sTable = 'Dim-BMI'
print('Loading:',sDatabaseName1,' Table:',sTable)
sSQL = "SELECT Height, Weight, Indicator FROM [Dim-BMI]"
sSQL = sSQL + " WHERE Indicator > 2"
sSQL = sSQL + " ORDER By Height, Weight;"
PersonFrame1 = pd.read_sql_query(sSQL, conn1)
DimPerson = PersonFrame1
DimPersonIndex = DimPerson.set_index(['Indicator'], inplace=False)

# Storing Island data into datamart
sTable = 'Dim-BMI-Vertical'
print('#'*65) 
print('Storing:',sDatabaseName2,' Table:',sTable)
print('#'*65) 
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")

# Loading again from datamart
sTable = 'Dim-BMI-Vertical'
print('Loading:', sDatabaseName2, 'Table:', sTable)
sSQL = "SELECT * FROM [Dim-BMI-Vertical];"
PersonFrame2 = pd.read_sql_query(sSQL, conn2)
print('#'*65) 

print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])