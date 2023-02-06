# 02B : Perform testing of hypothesis using two sample t-test

from scipy import stats
import numpy as np

data_group1 = np.array([14, 15, 15, 16, 13, 8, 14,
                        17, 16, 14, 19, 20, 21, 15,
                        15, 16, 16, 13, 14, 12])

data_group2 = np.array([40, 45, 55, 17, 14, 8, 12,
                        19, 19, 55, 17, 77, 24, 16,
                        13, 33, 13, 66, 15, 13])

print('Data Group1 :', data_group1, '\n')
print('Data Group2 :', data_group2, '\n')
stat,pval = stats.ttest_ind(a=data_group1, b=data_group2, equal_var=True)
print('pval :', pval, '\n')

if pval < 0.05:
  print("we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")