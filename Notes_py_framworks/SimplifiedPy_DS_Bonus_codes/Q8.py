# Q8. 8. Create a boxplot of given scores.
import seaborn as sns
import matplotlib.pyplot as plt
data = [80, 85, 90, 95, 100, 75, 60, 88]
sns.boxplot(data=data)
plt.show()