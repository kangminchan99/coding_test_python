def solution(x):
    result = 0
    for i in str(x):
        result += int(i)
    
    
    return True if x % result == 0 else False
        