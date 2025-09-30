# Q9. 9. Create a pairplot using the Iris dataset.
import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species')
plt.show()