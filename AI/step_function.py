import numpy as np
import matplotlib.pyplot as plt

# # 일반적인 계단함수
# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

# 계단함수 그래프
def step_function(x):
    y = x > 0 
    return np.array(x > 0, dtype= int)


def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y


x = np.arange(-5.0, 5.0, 0.01)
y_s = sigmoid(x)

plt.plot(x, step_function(x))
plt.plot(x, y_s)
plt.ylim(-0.1, 1.1)
plt.show()






    