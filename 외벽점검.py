import math
# 순열 만들기
import itertools

def solution(n, weak, dist):
    weakSize = len(weak)
    weak = weak + [w + n for w in weak]
    minCnt = math.inf
    
    # 취약점을 시작위치로 선정
    for start in range(weakSize):
        # dist에 대한 모든 순열을 만들어줌
        for d in itertools.permutations(dist, len(dist)):
            cnt = 1
            pos = start
            for i in range(1, weakSize):
                nextPos = start + i
                diff = weak[nextPos] - weak[pos]
                if diff > d[cnt-1]:
                    pos = nextPos
                    cnt += 1
                    if cnt > len(dist):
                        break
            
            
            if cnt <= len(dist):
                minCnt = min(minCnt, cnt)
                
                
    if minCnt == math.inf:
        return -1
        
        
        

    return minCnt
        