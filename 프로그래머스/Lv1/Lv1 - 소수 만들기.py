
from itertools import combinations

def solution(nums):
    # 리스트에서 3개의 숫자를 조합해서 나올 수 있는 모든 배열을 구하는 방법
    combiList = list(combinations(nums, 3))

    answer = 0
    for i in range(len(combiList)):
        hap = combiList[i][0] + combiList[i][1] + combiList[i][2]
        cnt = 0
        for i in range(1, hap):
            if hap % i == 0:
                cnt += 1
        if cnt == 1:
            answer += 1
    
    return answer