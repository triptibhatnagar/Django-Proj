# Q16. 16. Use scipy.optimize.minimize to find the minimum of f(x) = x^2 + 5*sin(x).
from scipy.optimize import minimize
import numpy as np
res = minimize(lambda x: x**2 + 5*np.sin(x), x0=0)
print(res.x)