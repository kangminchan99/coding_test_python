def solution(s):
    lent = len(s)
    
    if lent % 2 == 0 :
        result = lent // 2
        return s[result-1:result+1]
    else:
        result = lent // 2
        return s[result]