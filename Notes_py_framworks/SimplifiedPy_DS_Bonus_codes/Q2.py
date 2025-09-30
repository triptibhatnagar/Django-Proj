# Q2. 2. Group employee data by department and compute average salary.
import pandas as pd
df = pd.DataFrame({
'department': ['HR', 'IT', 'HR', 'IT'],
'salary': [30000, 40000, 35000, 45000]
})
print(df.groupby('department')['salary'].mean())