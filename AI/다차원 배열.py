import numpy as np

# 1차원
A = np.array([1, 2, 3, 4])
# print(A)
print(np.ndim(A))
print(A.shape[0])

# 2차원
B = np.array(([1, 2],[3, 4], [5, 6]))
print(B)
print(np.ndim(B))
print(B.shape[0])

# 3차원
C = np.array((([1, 2],[3, 4], [5, 6]),([1, 2],[3, 4], [5, 6])))
print(C)
print(np.ndim(C))
print(C.shape[0])


# 행렬의 곱
D = np.array(([1, 2],[3, 4]))
E = np.array(([5, 6],[7, 8]))
print(np.dot(D, E))
print(np.dot(E, D))

F = np.array(([1, 2, 3], [4, 5, 6]))
G = np.array((([1, 2], [3, 4], [5, 6])))
print(np.dot(F, G))





