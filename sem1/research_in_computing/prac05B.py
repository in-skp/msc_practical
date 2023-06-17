# 05B : Perform stratified sampling for the given data and analyze it

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split

plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

color = sns.color_palette()
sns.set_style('darkgrid')

housing = pd.read_csv('content/Housing.csv')
print(housing.head())
print(housing.info())

correlation_matrix = housing.corr()
plt.subplots(figsize=(8,6))
sns.heatmap(correlation_matrix, center=0, annot=True, linewidths=0.3)

corr = housing.corr()
#print(correlation_matrix)
print(corr['stories'].sort_values(ascending=False))

sns.displot(housing.stories)
plt.show()