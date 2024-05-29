def solution(before, after):
    bdic = {}
    
    for i in before:
        if i not in bdic:
            bdic[i] = 1
        else:
            bdic[i] += 1
            
    
    for i in after:
        if i not in bdic:
            return 0
        else:
            bdic[i] -= 1
            
    if max(bdic.values()) > 0:
        return 0
    else:
        return 1
