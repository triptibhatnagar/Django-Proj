# Q3. 3. Merge two DataFrames and fill missing values with 0.
import pandas as pd
df1 = pd.DataFrame({'id': [1, 2], 'math': [90, 80]})
df2 = pd.DataFrame({'id': [2, 3], 'science': [70, 85]})
result = pd.merge(df1, df2, on='id', how='outer')
result = result.fillna(0)
print(result)