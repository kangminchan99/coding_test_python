def solution(a, b):
    oddNum = 0
    
    oddNum += 1 if a % 2 != 0 else 0
    oddNum += 1 if b % 2 != 0 else 0
    
    if oddNum == 0:
        return abs(a - b)
    elif oddNum == 1:
        return 2 * (a + b)
    else:
        return a * a + b * b