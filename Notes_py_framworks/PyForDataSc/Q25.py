# Q25. 25. Create a pandas DataFrame and write it to a CSV file.
import pandas as pd
df = pd.DataFrame({'name': ['A', 'B'], 'marks': [90, 80]}) # 2 columns (name, marks)
df.to_csv('students.csv', index=False) # index=False → row numbers file me save nahi honge.