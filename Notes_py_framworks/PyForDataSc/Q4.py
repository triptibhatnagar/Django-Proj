# Q4. 4. Count missing values column-wise using pandas.

import pandas as pd
df = pd.read_csv('data.csv')
print(df.isnull().sum())

'''
isnull() → check karta hai ki DataFrame ke har cell me missing value hai ya nahi.
Missing value ka matlab NaN (Not a Number), None, ya khali cell.
Ye ek True/False table banata hai.
True → agar value missing hai.
False → agar value present hai.

.sum()
Jab aap True/False values pe .sum() use karte ho, Python unko 1 aur 0 ke tarah count karta hai.
True = 1
False = 0
Iska matlab har column me kitne True (yaani missing values) hai wo count ho jata hai.
'''