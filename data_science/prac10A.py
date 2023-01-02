"""
Created on Mon Jan 02

@author: Santosh Parse
@program name: Processing Data - Build the time Hub, Link and Satellite
"""
import sys
import os
from datetime import datetime
from datetime import timedelta
from pytz import timezone, all_timezones
import pandas as pd
import sqlite3 as sq
from pandas.io import sql
import uuid

pd.options.mode.chained_assignment = None

if sys.platform == 'linux':
    Base = os.path.expanduser('~') + 'VKHCG'
else:
    Base = 'C:/VKHCG'
print('#'*65) 
print("Working Base: ", Base, 'using', sys.platform)
print('#'*65)

Company='03-Hillman'
InputDir='00-RawData'
InputFileName='VehicleData.csv'

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

base = datetime(2023,1,1,0,0,0)
numUnits=2*24
date_list = [base - timedelta(hours=x) for x in range(0, numUnits)]
t=0
for i in date_list:
    now_utc=i.replace(tzinfo=timezone('UTC'))
    sDateTime=now_utc.strftime("%Y-%m-%d %H:%M:%S")  
    print(sDateTime)
    sDateTimeKey=sDateTime.replace(' ','-').replace(':','-')
    t+=1
    IDNumber=str(uuid.uuid4())
    TimeLine=[('ZoneBaseKey', ['UTC']),
             ('IDNumber', [IDNumber]),
             ('nDateTimeValue', [now_utc]),
             ('DateTimeValue', [sDateTime]),
             ('DateTimeKey', [sDateTimeKey])]
    if t==1:
       TimeFrame = pd.DataFrame.from_dict(dict(TimeLine))
    else:
        TimeRow = pd.DataFrame.from_dict(dict(TimeLine))
        TimeFrame = pd.concat([TimeFrame, TimeRow])
TimeHub=TimeFrame[['IDNumber','ZoneBaseKey','DateTimeKey','DateTimeValue']]
TimeHubIndex=TimeHub.set_index(['IDNumber'],inplace=False)
TimeFrame.set_index(['IDNumber'],inplace=True)

sTable = 'Process-Time'
print('Storing :',sDatabaseName1,' Table:',sTable)
TimeHubIndex.to_sql(sTable, conn1, if_exists="replace")

sTable = 'Hub-Time'
print('Storing :',sDatabaseName2,' Table:',sTable)
TimeHubIndex.to_sql(sTable, conn2, if_exists="replace")

active_timezones=all_timezones
z=0
for zone in active_timezones:    
    t=0
    for j in range(TimeFrame.shape[0]):
        now_date=TimeFrame['nDateTimeValue'][j]
        DateTimeKey=TimeFrame['DateTimeKey'][j]
        now_utc=now_date.replace(tzinfo=timezone('UTC'))
        sDateTime=now_utc.strftime("%Y-%m-%d %H:%M:%S")
        now_zone = now_utc.astimezone(timezone(zone))
        sZoneDateTime=now_zone.strftime("%Y-%m-%d %H:%M:%S")  
        t+=1
        z+=1
        IDZoneNumber=str(uuid.uuid4())
        TimeZoneLine=[('ZoneBaseKey', ['UTC']),
                      ('IDZoneNumber', [IDZoneNumber]),
                      ('DateTimeKey', [DateTimeKey]),
                      ('UTCDateTimeValue', [sDateTime]),
                      ('Zone', [zone]),
                      ('DateTimeValue', [sZoneDateTime])]
        if t==1:
           TimeZoneFrame = pd.DataFrame.from_dict(dict(TimeZoneLine))
        else:
            TimeZoneRow = pd.DataFrame.from_dict(dict(TimeZoneLine))
            TimeZoneFrame = pd.concat([TimeZoneFrame, TimeZoneRow])
    TimeZoneFrameIndex=TimeZoneFrame.set_index(['IDZoneNumber'],inplace=False)
    sZone=zone.replace('/','-').replace(' ','')

sTable = 'Process-Time-'+sZone
print('Storing :',sDatabaseName1,' Table:',sTable)
TimeZoneFrameIndex.to_sql(sTable, conn1, if_exists="replace")

sTable = 'Satellite-Time-'+sZone
print('Storing :',sDatabaseName2,' Table:',sTable)
TimeZoneFrameIndex.to_sql(sTable, conn2, if_exists="replace")

print('#'*65)
print('Vacuum Databases')
sSQL="VACUUM;"
sql.execute(sSQL,conn1)
sql.execute(sSQL,conn2)
print('#'*28 + ' Done!!! ' + '#'*28)

