def solution(sides):
#     가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
    maxS = sorted(sides)
    answer = 0
    
    # 가장 긴 변이 sides의 최댓값일 경우
    for i in range(1, maxS[1] + 1):
        if i + maxS[0] > maxS[1]:
            answer += 1
            
    # 나머지 한 변이 가장 긴 변인 경우
    for i in range(maxS[1] + 1, maxS[0] + maxS[1]):
        answer += 1
            
    return answer