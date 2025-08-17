# Q24. 24. Use subplots in matplotlib to show multiple plots.
import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot([1,2,3])
axs[0, 1].bar([1,2,3], [3,2,1])
axs[1, 0].scatter([1,2], [2,1])
axs[1, 1].hist(np.random.randn(100))
# plt.tight_layout()
plt.show()