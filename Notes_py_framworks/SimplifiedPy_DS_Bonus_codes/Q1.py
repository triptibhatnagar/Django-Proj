# Q1. 1. Use lambda to square each element in a column 'marks'.
import pandas as pd
df = pd.DataFrame({'marks': [10, 20, 30]})
df['squared'] = df['marks'].apply(lambda x: x * x)
print(df)