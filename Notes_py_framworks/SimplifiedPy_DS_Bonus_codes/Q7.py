# Q7. 7. Plot correlation heatmap using seaborn.
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
sns.heatmap(df.corr(), annot=True)
plt.show()