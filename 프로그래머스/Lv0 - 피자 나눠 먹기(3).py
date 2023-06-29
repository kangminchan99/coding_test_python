import math

def solution(slice, n):
    sum = 0
    if slice > n:
        sum = 1
    else:
        if n % slice == 0:
            sum = n / slice
        else:
            sum = math.ceil(n / slice)
    
    return sum