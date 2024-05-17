def solution(a, b, n):
    bottle = n
    result = 0
    while bottle >= a:
        cola = (bottle // a) * b
        bottle = cola + bottle % a
        result += cola
        
    return result
        
        
        
