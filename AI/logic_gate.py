import numpy as np

def AND(x1, x2):
#    w1, w2, theta = 0.5, 0.5, 0.7
#    tmp = x1 * w1 + x2 * w2
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1    

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

A = 1
B = 1
C = 1

M_1 = XOR(A, B)
M_2 = AND(M_1, C)
M_3 = AND(A, B)

SUM = XOR(M_1 , C)
Cout = OR(M_2, M_3)

print('M_1', M_1)
print('M_2', M_2)
print('M_3', M_3)
print('sum = ',SUM)
print('Cout = ',Cout)