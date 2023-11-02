import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
a = np.array([1000, 1100, 990])


c = np.max(a)
# a = np.array([0.3, 2.9, 4.0])

print(softmax(a))