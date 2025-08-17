# Q19. 19. Compute eigenvalues and eigenvectors of a matrix using scipy.linalg.eig.
import numpy as np
A = np.array([[1,2],[3,4]])
vals, vecs = np.linalg.eig(A)
print("Eigenvalues:", vals)
print("Eigenvectors:", vecs)