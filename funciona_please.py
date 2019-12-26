import numpy as np
from SCSA import SCSA
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.025)
h = np.arange(0.1, 3, 0.01)
error = np.zeros(len(h))
data = np.square(np.sin(x)) + 1
for i in range(len(h)):
    holder = SCSA(data, h[i])
    error[i] = holder.mse
print(h[error == min(error)])
holder = SCSA(data, h[error == min(error)])
plt.plot(holder.reconstructed)
plt.plot(data)
plt.show()