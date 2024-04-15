from itertools import combinations

def solution(number):
    combiList = list(combinations(number, 3))
    cnt = 0
    for i in combiList:
        if sum(i) == 0:
            cnt += 1
    
    return cnt
    