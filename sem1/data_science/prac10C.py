"""
Created on Mon Jan 02

@author: Santosh Parse
@program name: Processing Data - Forecasting
"""
import sys
import os
import sqlite3 as sq
import quandl
import pandas as pd

if sys.platform == 'linux':
    Base = os.path.expanduser('~') + 'VKHCG'
else:
    Base = 'C:/VKHCG'
print('#'*65) 
print("Working Base: ", Base, 'using', sys.platform)
print('#'*65)

Company='04-Clark'
sInputFileName='00-RawData/VKHCG_Shares.csv'
sOutputFileName='Shares.csv'

sDataBaseDir=Base + '/' + Company + '/03-Process/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)

sFileDir1=Base + '/' + Company + '/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir1):
    os.makedirs(sFileDir1)

sFileDir2=Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir2):
    os.makedirs(sFileDir2)

sFileDir3=Base + '/' + Company + '/03-Process/01-EDS/02-Python'
if not os.path.exists(sFileDir3):
    os.makedirs(sFileDir3)

sDatabaseName=sDataBaseDir + '/clark.db'
conn = sq.connect(sDatabaseName)

# Import Share Names Data
sFileName=Base + '/' + Company + '/' + sInputFileName
print('Loading :',sFileName)
print('#'*65)
RawData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
RawData.drop_duplicates(subset=None, keep="first", inplace=True)
print('Rows   :',RawData.shape[0])
print('Columns:',RawData.shape[1])

sFileName=sFileDir1 + '/Retrieve_' + sOutputFileName
print('#'*65)
print('Storing :', sFileName)
print('#'*65)
RawData.to_csv(sFileName, index = False)

sFileName=sFileDir2 + '/Assess_' + sOutputFileName
print('Storing :', sFileName)
print('#'*65)
RawData.to_csv(sFileName, index = False)

sFileName=sFileDir3 + '/Process_' + sOutputFileName
print('Storing :', sFileName)
print('#'*65)
RawData.to_csv(sFileName, index = False)

# Import Shares Data Details
for sShare in range(RawData.shape[0]):
    if sShare == 1:
        break;
    sShareName=str(RawData['Shares'][sShare])
    ShareData = quandl.get(sShareName)
    UnitsOwn=RawData['Shares'][sShare]
    ShareData['UnitsOwn']=ShareData.apply(lambda row:(UnitsOwn),axis=1)  
    print('#'*65)
    print('Share  :',sShareName)
    print('Rows   :',ShareData.shape[0])
    print('Columns:',ShareData.shape[1])
    print('#'*65)
    sTable=str(RawData['sTable'][sShare])
    sTable=sTable.replace("/","_")
    print('Storing :',sDatabaseName,' Table:',sTable)
    ShareData.to_sql(sTable, conn, if_exists="replace")
    print('#'*65)

    sOutputFileName = sTable + '.csv'
    sFileName=sFileDir1 + '/Retrieve_' + sOutputFileName
    print('Storing :', sFileName)
    print('#'*65)
    RawData.to_csv(sFileName, index = False)

    sOutputFileName = sTable + '.csv'
    sFileName=sFileDir2 + '/Assess_' + sOutputFileName
    print('#'*65)
    print('Storing :', sFileName)
    print('#'*65)
    RawData.to_csv(sFileName, index = False)

    sOutputFileName = sTable + '.csv'
    sFileName=sFileDir3 + '/Process_' + sOutputFileName
    print('#'*65)
    print('Storing :', sFileName)
    print('#'*65)
    RawData.to_csv(sFileName, index = False)

print('#'*28 + ' Done!!! ' + '#'*28)
