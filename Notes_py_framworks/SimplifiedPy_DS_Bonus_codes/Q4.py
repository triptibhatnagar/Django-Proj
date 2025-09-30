# Q4. 4. Detect, fill, and drop missing values in a column.
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [1, np.nan, 3, None]})
print(df.isnull())
print(df.fillna(0))
print(df.dropna())