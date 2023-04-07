#6B : Perform testing of hypothesis using two way ANOVA

import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np
import pandas as pd

df = pd.DataFrame({'Fertilizer': np.repeat(['daily','weekly'], 15),
                   'Watering': np.repeat(['daily', 'weekly'], 15),
                   'height': [14, 16, 15, 15, 16, 13, 12, 11,
                              14, 15, 16, 16, 17, 18, 14, 13,
                              14, 14, 14, 15, 16, 16, 17, 18,
                              14, 13, 14, 14, 14, 14]})

model = ols('height ~ C(Fertilizer) + C(Watering) + C(Fertilizer):C(Watering)', data=df).fit()

result = sm.stats.anova_lm(model, type=2)

print(result)