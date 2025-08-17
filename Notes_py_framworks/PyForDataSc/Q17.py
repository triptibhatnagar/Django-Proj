# Q17. 17. Integrate f(x) = x^2 from 0 to 1 using scipy.integrate.quad().
from scipy.integrate import quad
f = lambda x: x**2

result, _ = quad(f, 0, 1) # quad() returns tuple → (integral value, error estimate)
print("Integral:", result)