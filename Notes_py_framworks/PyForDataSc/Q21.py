# Q21. 21. Group data by a column and compute mean salary.
import pandas as pd
df = pd.DataFrame({'dept': ['HR','IT','HR','IT'], 'salary':[30000,40000,35000,45000]})
print(df.groupby('dept').mean())