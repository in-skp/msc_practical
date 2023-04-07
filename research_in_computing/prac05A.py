# 05A : Perform random sampling for the given data and analyze it.

import random
import pandas as pd

# create list of 5 numbers
num_list = random.sample(range(100), 10)
random.shuffle(num_list)
print(num_list)

# Randomly sample 10 data values from housing dataset
housing = pd.read_csv('content/Housing.csv')
df1 = pd.DataFrame(housing)
housing_list = df1.sample(10)
print(housing_list)

# Randomly sample 5 values from bathroom
df2 = pd.DataFrame(housing,  columns = ['bathrooms'])
bathrooms_list = df2.sample(5)
print(bathrooms_list)
