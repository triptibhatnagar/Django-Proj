# Q26. 26. Implement one-hot encoding on a categorical column using pandas.
import pandas as pd
df = pd.DataFrame({'color': ['red', 'green', 'blue', 'red']})
df_encoded = pd.get_dummies(df, dtype=int)
print(df_encoded)

# One-Hot Encoding me har unique category ke liye ek naya column ban jata hai, aur us row me 1 (True) dalte hain jisme vo category present hai, baaki sab me 0 (False)