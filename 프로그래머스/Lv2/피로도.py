# from itertools import combinations
# 순열
from itertools import permutations
def solution(k, dungeons):

#   순열로 리스트 생성
    permList = list(permutations(dungeons, len(dungeons)))
    maxCnt = 0
#   순열 길이
    lenPerm = len(permList)
    for i in range(lenPerm):
        #   던전 체크
        checkCnt = 0
        checkK = k
        for j in permList[i]:

            if checkK >= j[0]:
                checkK -= j[1]
                checkCnt += 1

            if checkCnt > maxCnt:
                maxCnt = checkCnt
    return maxCnt
            