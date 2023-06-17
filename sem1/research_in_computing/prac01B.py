# 01B : Import data from different data sources (from Excel, csv, mysql, sql server, oracle to R/Python/Excel).

# From CSV
import pandas as pd

print('********Read From CSV********')
df1 = pd.read_csv('content/Ages.csv')
print(df1.head())

# From Excel
print('*******Read From Excel*******')
df2 = pd.read_excel('content/Ages.xlsx')
print(df2.head())

# From json
print('********Read From JSON********')
df3 = pd.read_json('content/sample.json')
print(df3.head())