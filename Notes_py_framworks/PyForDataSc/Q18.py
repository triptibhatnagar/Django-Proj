# Q18. 18. Apply a high-pass filter using scipy.signal.butter and filtfilt.
from scipy.signal import butter, filtfilt
import numpy as np
b, a = butter(4, 0.2, 'high')
data = np.random.rand(100)
filtered = filtfilt(b, a, data)
print(filtered)