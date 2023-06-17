# 02C : Perform testing of hypothesis using paired test 

from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('content/blood_pressure.csv')

print(df[['bp_before', 'bp_after']].describe())

# First lets check for outliers
df[['bp_before', 'bp_after']].plot(kind='box')

plt.savefig('boxplot_outliers.png')

df['bp_difference'] = df['bp_before'] - df['bp_after']

df['bp_difference'].plot(kind='hist', title='Blodd Pressure Difference Histogram')

plt.savefig('blood pressure difference histogram.png')

stats.probplot(df['bp_difference'], plot=plt)
plt.title('Blood pressure difference Q-Q Plot')
plt.savefig('blood pressure difference qq plot.png')
stats.shapiro(df['bp_difference'])
stat, pval = stats.ttest_rel(df['bp_before'], df['bp_after'])
print('\npval :', pval)