# Q6. 6. Add a new column and then delete it.
import pandas as pd

df = pd.DataFrame({'name': ['A', 'B'], 'score': [80, 90]})
df['grade'] = ['B', 'A']
print(df)
df = df.drop('grade', axis=1)
print(df)