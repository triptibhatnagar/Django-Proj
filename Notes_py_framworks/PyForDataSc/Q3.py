# Q3. 3. Load a `.csv` file using pandas and display the first 5 rows.
# ek table jaisa structure (rows aur columns) jisme data store hota hai. = DataFrame

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())