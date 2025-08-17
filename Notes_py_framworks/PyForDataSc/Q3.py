# Q3. 3. Load a `.csv` file using pandas and display the first 5 rows.
# Excel sheet jaisi cheez Python ke andar = DataFrame

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())