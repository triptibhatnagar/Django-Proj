# Q13. 13. Perform element-wise multiplication and dot product of two 2D arrays.
import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[2,0],[1,2]])
print("Element-wise:", a * b)
print("Dot product:", np.dot(a, b))