# Q27. 27. Simulate missing data and apply forward-fill and backward-fill.
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [1, np.nan, 3, None]}) # np.nan aur None dono ko pandas missing value (NaN) treat karega.
# print(df.fillna(method='ffill')) # missing value ko previous non-missing value se bhar do
# print(df.fillna(method='bfill')) # missing value ko next non-missing value se bhar do
# above methods are deprecated, so use below ones
print(df.ffill())
print(df.bfill())