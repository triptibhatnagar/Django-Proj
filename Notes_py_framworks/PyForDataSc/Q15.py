# Q15. 15. Solve a system of equations using scipy.linalg.solve().
from scipy.linalg import solve
import numpy as np
a = np.array([[3, 5],[1,2]])
b = np.array([9,8])
x = solve(a,b)
print(x)