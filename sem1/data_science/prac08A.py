"""
Created on Mon Jan 02

@author: Santosh Parse
@program name: Transforming Data - Building data warehouse
"""
import sys
import os
from datetime import datetime
from pytz import timezone
import pandas as pd
import sqlite3 as sq
import uuid

# chained_assignment mode change to None to supress SettingWithCopyWarning:
pd.options.mode.chained_assignment = None

if sys.platform == 'linux':
    Base = os.path.expanduser('~') + 'VKHCG'
else:
    Base = 'C:/VKHCG'
print('#'*65) 
print("Working Base: ", Base, 'using', sys.platform)
print('#'*65) 

Company = '01-Vermeulen'
sDataBaseDir = Base + '/' + Company + '/04-Transform/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
sDataBaseName1 = sDataBaseDir + '/Vermeulen.db'
conn1 = sq.connect(sDataBaseName1)

sDataWarehouseDir = Base + '/99-DW'
if not os.path.exists(sDataWarehouseDir):
    os.makedirs(sDataWarehouseDir)
sDataBaseName2 = sDataWarehouseDir + '/datawarehouse.db'
conn2 = sq.connect(sDataBaseName2)

print('Time Dimension')
BirthZone = 'Atlantic/Reykjavik'
BirthDateUTC = datetime(1960,12,20,10,15,0)
BirthDateZoneUTC = BirthDateUTC.replace(tzinfo=timezone('UTC'))
BirthDateZoneStr = BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S")
BirthDateZoneUTCStr = BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")
BirthDate = BirthDateZoneUTC.astimezone(timezone(BirthZone))
BirthDateStr = BirthDate.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")
BirthDateLocal = BirthDate.strftime("%Y-%m-%d %H:%M:%S")
IDTimeNumber = str(uuid.uuid4())
TimeLine=[('TimeID', [IDTimeNumber]),
          ('UTCDate', [BirthDateZoneStr]),
          ('LocalTime', [BirthDateLocal]),
          ('TimeZone', [BirthZone])]
TimeFrame = pd.DataFrame.from_dict(dict(TimeLine))
DimTime = TimeFrame
DimTimeIndex = DimTime.set_index(['TimeID'],inplace=False)

sTable = 'Dim-Time'
print('#'*65) 
print('Storing :',sDataBaseName1,'\nTable:',sTable)
DimTimeIndex.to_sql(sTable, conn1, if_exists="replace")
print('#'*65) 
print('Storing :',sDataBaseName2,'\nTable:',sTable)
DimTimeIndex.to_sql(sTable, conn2, if_exists="replace")

print('#'*65) 
print('Person Dimension')
FirstName = 'Guðmundur'
LastName = 'Gunnarsson'
IDPersonNumber=str(uuid.uuid4())
PersonLine=[('PersonID', [IDPersonNumber]),
              ('FirstName', [FirstName]),
              ('LastName', [LastName]),
              ('Zone', ['UTC']),
              ('DateTimeValue', [BirthDateZoneStr])]
PersonFrame = pd.DataFrame.from_dict(dict(PersonLine))
DimPerson=PersonFrame
DimPersonIndex=DimPerson.set_index(['PersonID'],inplace=False)
sTable = 'Dim-Person'
print('#'*65) 
print('Storing :',sDataBaseName1,'\nTable:',sTable)
DimPersonIndex.to_sql(sTable, conn1, if_exists="replace")
print('#'*65) 
print('Storing :',sDataBaseName2,'\nTable:',sTable)
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")

print('#'*65) 
print('Fact - Person - Time')
print('#'*65)
IDFactNumber=str(uuid.uuid4())
PersonTimeLine=[('IDNumber', [IDFactNumber]),
                ('IDPersonNumber', [IDPersonNumber]),
                ('IDTimeNumber', [IDTimeNumber])]
PersonTimeFrame = pd.DataFrame.from_dict(dict(PersonTimeLine))
FctPersonTime=PersonTimeFrame
FctPersonTimeIndex=FctPersonTime.set_index(['IDNumber'],inplace=False)
sTable = 'Fact-Person-Time'
print('Storing:',sDataBaseName1,'\nTable:',sTable)
FctPersonTimeIndex.to_sql(sTable, conn1, if_exists="replace")
print('#'*65)
print('Storing:',sDataBaseName2,'\nTable:',sTable)
FctPersonTimeIndex.to_sql(sTable, conn2, if_exists="replace")

