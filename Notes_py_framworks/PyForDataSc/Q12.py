# Q12. 12. Reshape a 3x4 array into 2x6 and flatten it.
import numpy as np
arr = np.arange(12).reshape(3, 4)
# np.arange(12) → 0 se 11 tak numbers generate karega.
# .reshape(3,4) → 3 rows aur 4 columns me arrange karega.
print(arr)
reshaped = arr.reshape(2, 6)
# .reshape(2,6) → array ko 2 rows aur 6 columns me convert karta hai.
print(reshaped)
flattened = reshaped.flatten()
print(flattened)