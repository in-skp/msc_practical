"""
Created on Wed Dec 28

@author: Santosh Parse
@program name: Write a program to convert CSV file format to HORUS format 
"""
import pandas as pd

# Input Agreement
sInputFileName = 'C:/VKHCG/05-DS/9999-Data/Country_Code.csv'
InputData = pd.read_csv(sInputFileName, encoding="latin-1")
print('='*65)
print('Input Data Values:')
print(InputData)
print('='*65)

# Processing Rules
ProcessData = InputData
ProcessData.drop('ISO-2-CODE', axis=1, inplace=True)
ProcessData.drop('ISO-3-Code', axis=1, inplace=True)
ProcessData.rename(columns={'Country' : 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49' : 'CountryNumber'}, inplace=True)
ProcessData.set_index('CountryNumber', inplace=True)
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)
print('Process Data Values')
print(ProcessData)

# Output Agreement
OutputData = ProcessData
sOutputFileName = 'C:/VKHCG/05-DS/9999-Data/HORUS-CSV-Country.csv'
OutputData.to_csv(sOutputFileName, index=False)
print('='*22 + ' CSV to HORUS - Done ' + '='*22) 