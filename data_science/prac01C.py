"""
Created on Sun Dec 25

@author: Santosh Parse
@program name: Keep only the rows that contain a maximum of two missing values. 
"""
import sys;
import os;
import pandas as pd;

if sys.platform == 'linux':
    Base = os.path.expanduser('~') + 'VKHCG'
else:
    Base = 'C:/VKHCG'
print('#'*65) 
print("Working Base: ", Base, 'using', sys.platform)
print('#'*65) 
sInputFileName = 'Good-or-Bad.csv'
sOutputFileName = 'Good-or-Bad-03.csv'
Company = '01-Vermeulen'

sFileDir = Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)

# Import Warehouse
sFileName = Base + '/' + Company + '/00-RawData/' + sInputFileName
print('Loading:', sFileName)
RawData = pd.read_csv(sFileName, header=0)
print('#'*65)   
print('## Raw Data Values')  
print('#'*65)  
print(RawData)
print('#'*65)   
print('## Data Profile Before Dropping Rows')
print('#'*65) 
print('Rows:',RawData.shape[0])
print('Columns:',RawData.shape[1])
print('#'*65) 
sFileName = sFileDir + '/' + sInputFileName
RawData.to_csv(sFileName, index=False)

# Keeps rows that contains maximum 2 missing values
TestData = RawData.dropna(thresh=2)
  
print('## Test Data Values')  
print('#'*65)  
print(TestData)
print('#'*65)  
print('## Data Profile After Dropping Rows')
print('#'*65)
print('Rows:',TestData.shape[0])
print('Columns:',TestData.shape[1])

sFileName = sFileDir + '/' + sOutputFileName
TestData.to_csv(sFileName, index=False)
print('#'*28 + ' Done!!! '+'#'*28)