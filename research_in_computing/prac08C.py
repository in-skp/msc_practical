#8C : Perform Spearmans Correlation
from numpy.random import randn
from numpy.random import seed
from scipy.stats import spearmanr
seed(1)
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

corr, _ = spearmanr(data1, data2)
print('Spearmans Correlation: %.3f' %corr)