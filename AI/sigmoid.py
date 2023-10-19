import numpy as np
import matplotlib.pyplot as plt;

# 범위
x = np.linspace(-5, 5)

def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y

plt.plot(x,sigmoid(x))
plt.show()

