from functools import cmp_to_key

def check(relation, rowsize, colsize, subset):
    for a in range(rowsize - 1):
        for b in range(a+1, rowsize):
            isSame = True
            for k in range(colsize):
                if (subset & 1 << k) == 0:
                    continue
                if relation[a][k] != relation[b][k]:
                    isSame = False
                    break
            if isSame:
                return False
    return True

def compare(a, b):
    x = bin(a).count('1')
    y = bin(b).count('1')
    return x - y
    

def solution(relation):
    answer = 0
    # 릴레이션 리스트의 길이
    rowSize = len(relation)
    # 속성의 개수
    colSize = len(relation[0])
    candidates = []
    # 후보키가 될 수 있는 것들을 비트로 표현
    for i in range(1, 1 << colSize):
        if check(relation, rowSize, colSize, i):
            candidates.append(i)
            
    candidates = sorted(candidates, key = cmp_to_key(compare))
    
    while len(candidates) != 0:
        n = candidates.pop(0)
        answer += 1
        candidates = [x for x in candidates if (n & x) != n]
        
    return answer
        