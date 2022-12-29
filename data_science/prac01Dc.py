"""
Created on Sun Dec 25

@author: Santosh Parse
@program name: Create a network routing diagram from the given data on the routers. 
                (Assess- Node) 
"""
import sys
import os
import pandas as pd

# chained_assignment mode change to None to supress SettingWithCopyWarning:
pd.options.mode.chained_assignment = None

if sys.platform == 'linux':
    Base = os.path.expanduser('~') + 'VKHCG'
else:
    Base = 'C:/VKHCG'
print('#'*65) 
print("Working Base: ", Base, 'using', sys.platform)
print('#'*65) 

# Initialize input and output
sInputFileName = '01-Retrieve/01-EDS/02-Python/Retrieve_IP_DATA.csv'
sOutputFileName = 'Assess-Network-Routing-Node.csv'
Company = '01-Vermeulen'

# Import IP Data
sFileName = Base + '/' + Company + '/' + sInputFileName
print('Loading:', sFileName)
print('#'*65)
IPData = pd.read_csv(sFileName, header=0, low_memory=False, encoding="latin-1")
print('Loaded IP:', IPData.columns.values)
print('#'*65)

# Assess IP Data
print('Changed:', IPData.columns.values)
IPData.drop('RowID', axis=1, inplace=True)
IPData.drop('ID', axis=1, inplace=True)
IPData.rename(columns={'Country' : 'Country_Code'}, inplace=True)
IPData.rename(columns={'Place.Name' : 'Place_Name'}, inplace=True)
IPData.rename(columns={'Post.Code' : 'Post_Code'}, inplace=True)
IPData.rename(columns={'First.IP.Number' : 'First_IP_Number'}, inplace=True)
IPData.rename(columns={'Last.IP.Number' : 'Last_IP_Number'}, inplace=True)
print('To:', IPData.columns.values)
print('#'*65)
print('Changed:', IPData.columns.values)
for i in IPData.columns.values:
    j = 'Node_' + i
    IPData.rename(columns={i:j}, inplace=True)
print('To:', IPData.columns.values)
sFileDir = Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
sFileName = sFileDir + '/' + sOutputFileName
print('#'*65)
print('Storing:', sFileName)
IPData.to_csv(sFileName, index=False, encoding="latin-1")
print('#'*28 + ' Done!!! '+'#'*28)
