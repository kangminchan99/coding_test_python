import math

def solution(array):
    a = sorted(array)
    b = math.ceil(len(a) / 2) - 1
    return a[b]

