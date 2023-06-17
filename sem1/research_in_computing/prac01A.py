# 01A : Write a program fro obtaining descriptive statistics for data in google colab and excel

import pandas as pd
import numpy as np

# Create Dictionary of data
d = {'Name': pd.Series(['Santosh', 'Prashant', 'Ram', 'Bilal', 'Aftab', 'Pavitra', 'Ankita', 'Reena', 'Neha', 'Komal']),
     'Age': pd.Series([35,28,30,30,22,28,24,28,26,27]),
     'Rating': pd.Series([4.2, 4.5, 3.3, 4.5, 3.98, 4, 3, 3.1, 4.3, 4.4])
     }

# Create a DataFrame
df = pd.DataFrame(d)

# Print DataFrame
print('********Data Frame********')
print(df,'\n')

# Print DataFrame Sum
print('********Sum********')
print(df.sum(), '\n')

# Print DataFrame Sum with axis = 1
print('********Sum with axis=1********')
print(df[['Age','Rating']].sum(1), '\n')

# Print DF mean
print('********Mean********')
print(df[['Age','Rating']].mean(), '\n')

# Print DF Standard Deviation
print('********Standard Deviation********')
print(df[['Age','Rating']].std(), '\n')

# Print Data Summary
print('********Descriptive Statistics********')
print(df.describe())