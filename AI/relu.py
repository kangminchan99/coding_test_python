import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)




def step_function(x):
    y = x > 0 
    return np.array(x > 0, dtype= int)


def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y


x = np.arange(-5.0, 5.0, 0.1)
y_s = sigmoid(x)
y_r = relu(x)

plt.plot(x, step_function(x))
plt.plot(x, y_s)
plt.plot(x, y_r)
plt.ylim(-0.1, 10.1)
plt.show()


