# Q11. 11. Generate a 1D NumPy array of 50 random numbers and plot a histogram using matplotlib.
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(50)
# data = np.array([1,92,3,34,5,6,67,82,9,10])
print(data)
plt.hist(data)
plt.show()