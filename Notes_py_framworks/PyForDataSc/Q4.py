# Q4. 4. Count missing values column-wise using pandas.

import pandas as pd
df = pd.read_csv('data.csv')
print(df.isnull().sum())

'''
df.isnull() → returns a DataFrame of booleans (True if value is missing, else False).
.sum() (without axis argument) → by default, sums column-wise.

Since True = 1 and False = 0, the result is the count of missing values per column.

So df.isnull().sum() returns a pandas Series where:
Index = column names
Values = number of missing values in each column

Now about dtype:
dtype means data type of the values in the Series/DataFrame column.
In this case, df.isnull().sum() produces integer counts.
Therefore, the result Series will have dtype: int64 (most common in pandas).
'''