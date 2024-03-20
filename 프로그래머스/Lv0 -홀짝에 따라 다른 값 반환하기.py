def solution(n):
    sum1 = 0
    mul1 = 0
    
    for i in range(n + 1):
        if i % 2 != 0:
            sum1 += i
        else:
            mul1 += i*i
    
    return sum1 if i % 2 != 0 else mul1