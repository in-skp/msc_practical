# 02A : Perform testing of hypothesis using one sample t-test

from scipy.stats import ttest_1samp
import numpy as np

ages = np.genfromtxt('content\Ages.csv')
print(ages)
ages_mean = np.mean(ages)
print(ages_mean)
tset, pval = ttest_1samp(ages, 36)
print('p-values -', pval)

if pval < 0.05:
  print("we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")