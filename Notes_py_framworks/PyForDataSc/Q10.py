# Q10. 10. Create a 3x3 matrix in NumPy and compute its transpose and determinant.
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Transpose:", A.T)
print("Determinant:", np.linalg.det(A))