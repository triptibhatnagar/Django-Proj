# Q23. 23. Merge two DataFrames and fill NaN with defaults.
import pandas as pd
import numpy as np
df1 = pd.DataFrame({'id':[1,2], 'val1':[10,20]})
df2 = pd.DataFrame({'id':[1,2], 'val2':[np.nan,40]})
merged = pd.merge(df1, df2, on='id', how='outer').fillna(0) # outer join: dono DataFrames ke saare rows include honge.
print(merged)