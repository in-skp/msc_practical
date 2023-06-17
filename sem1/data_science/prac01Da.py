"""
Created on Sun Dec 25

@author: Santosh Parse
@program name: Create a network routing diagram from the given data on the routers. 
                (Assess- Company) 
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
sInputFileName1 = '01-Retrieve/01-EDS/01-R/Retrieve_Country_Code.csv'
sInputFileName2 = '01-Retrieve/01-EDS/02-Python/Retrieve_Router_Location.csv'
sOutputFileName = 'Assess-Network-Routing-Company.csv'
Company = '01-Vermeulen'

# Import Country Data
sFileName = Base + '/' + Company + '/' + sInputFileName1
print('Loading:', sFileName)
print('#'*65)

CountryData = pd.read_csv(sFileName, header=0, low_memory=False, encoding="latin-1")
print('Loaded Country:', CountryData.columns.values)
print('#'*65)

# Assess Country Data
print('Changed:', CountryData.columns.values)
CountryData.rename(columns={'Country':'Country_Name'}, inplace=True)
CountryData.rename(columns={'ISO-2-CODE':'Country_Code'}, inplace=True)
CountryData.drop('ISO-M49', axis=1, inplace=True)
CountryData.drop('ISO-3-Code', axis=1, inplace=True)
CountryData.drop('RowID', axis=1, inplace=True)
print('To:',CountryData.columns.values)
print('#'*65)

# Import Company Data
sFileName = Base + '/' + Company + '/' + sInputFileName2
print('Loading:', sFileName)
print('#'*65)
CompanyData = pd.read_csv(sFileName, header=0, low_memory=False, encoding="latin-1")
print('Loaded Company:', CompanyData.columns.values)
print('#'*65)

# Assess Company Data
print('Changed:', CompanyData.columns.values)
CompanyData.rename(columns={'Country':'Country_Code'}, inplace=True)
print('To:', CompanyData.columns.values)
print('#'*65)

# Merge Company and Country Data
print('Merge Company and Country Data')
CompanyNetworkData = pd.merge(CompanyData, CountryData, how="inner", on="Country_Code")
print('#'*65)
print('Changed:', CompanyNetworkData.columns.values)
for i in CompanyNetworkData.columns.values:
    j = 'Company_' + i
    CompanyNetworkData.rename(columns={i:j}, inplace=True)
print('To:', CompanyNetworkData.columns.values)
sFileDir = Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
sFileName = sFileDir + '/' + sOutputFileName
print('#'*65)
print('Storing:', sFileName) 
CompanyNetworkData.to_csv(sFileName, index=False, encoding="latin-1")
print('#'*28 + ' Done!!! '+'#'*28)