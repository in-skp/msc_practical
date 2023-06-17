#6C : Perform testing of hypothesis using MANOVA 
import pandas as pd
from statsmodels.multivariate.manova import MANOVA
#url='https://vincentarelbundock.github.io/Rdatasets/csv/datasets/iris.csv'
url='content/iris.csv'
df= pd.read_csv(url, index_col=0)
df.columns = df.columns.str.replace(".","_")
df.head()
maov=MANOVA.from_formula('Sepal_Length+Sepal_Width+Petal_Length+Petal_Width ~Species',data=df)
print(maov.mv_test())