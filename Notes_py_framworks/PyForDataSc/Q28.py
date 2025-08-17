# Q28. 28. Create a correlation matrix plot from a DataFrame.
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.DataFrame(np.random.randn(10, 5), columns=list('ABCDE'))
sns.heatmap(df.corr(), annot=True) # df.corr() -> correlation matrix banata hai, annot=True -> har cell ke andar number likh deta hai
plt.show()

# Heatmap ek data visualization technique hai jisme numerical values ko colors ke through dikhaya jata hai