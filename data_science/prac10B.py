"""
Created on Mon Jan 02

@author: Santosh Parse
@program name: Processing Data - Human-Environment Interaction
"""
import sys
import os
import pandas as pd
import networkx as nx
import sqlite3 as sq
from pandas.io import sql
import uuid

if sys.platform == 'linux':
    Base = os.path.expanduser('~') + 'VKHCG'
else:
    Base = 'C:/VKHCG'
print('#'*65) 
print("Working Base: ", Base, 'using', sys.platform)
print('#'*65)

Company='01-Vermeulen'
InputAssessGraphName='Assess_All_Animals.gml'
EDSAssessDir='02-Assess/01-EDS'
InputAssessDir=EDSAssessDir + '/02-Python'

sFileAssessDir=Base + '/' + Company + '/' + InputAssessDir
if not os.path.exists(sFileAssessDir):
    os.makedirs(sFileAssessDir)

sDataBaseDir=Base + '/' + Company + '/03-Process/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
sDatabaseName1=sDataBaseDir + '/Hillman.db'
conn1 = sq.connect(sDatabaseName1)

sDataVaultDir=Base + '/88-DV'
if not os.path.exists(sDataVaultDir):
    os.makedirs(sDataVaultDir)
sDatabaseName2=sDataVaultDir + '/datavault.db'
conn2 = sq.connect(sDatabaseName2)

t=0
tMax=1*180

for Longitude in range(160,180,1):
    for Latitude in range(70,90,1):
        t+=1
        IDNumber=str(uuid.uuid4())
        LocationName='L'+format(round(Longitude,3)*1000, '+07d') +\
                                '-'+format(round(Latitude,3)*1000, '+07d')
        # print('Create:',t,' of ',tMax,':',LocationName)
        LocationLine=[('ObjectBaseKey', ['GPS']),
                     ('IDNumber', [IDNumber]),
                     ('LocationNumber', [str(t)]),
                     ('LocationName', [LocationName]),
                     ('Longitude', [Longitude]),
                     ('Latitude', [Latitude])]
        if t==1:
            LocationFrame = pd.DataFrame.from_dict(dict(LocationLine))
        else:
            LocationRow = pd.DataFrame.from_dict(dict(LocationLine))
            LocationFrame = pd.concat([LocationFrame, LocationRow])

LocationHubIndex=LocationFrame.set_index(['IDNumber'],inplace=False)

sTable = 'Process-Location'
print('Storing :',sDatabaseName1,'\nTable:',sTable)
LocationHubIndex.to_sql(sTable, conn1, if_exists="replace")
print('#'*65)

sTable = 'Hub-Location'
print('Storing :',sDatabaseName2,'\nTable:',sTable)
LocationHubIndex.to_sql(sTable, conn2, if_exists="replace")

print('#'*65)
print('Vacuum Databases')
sSQL="VACUUM;"
sql.execute(sSQL,conn1)
sql.execute(sSQL,conn2)
print('#'*28 + ' Done!!! ' + '#'*28)

