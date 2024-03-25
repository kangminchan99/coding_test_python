def solution(intStrs, k, s, l):
    answer = []
    add = []
    
    for i in intStrs:
        add.append(i[s: s + l])
    
    for i in add:
        if int(i) > k:
            answer.append(int(i))
    
#   문자열 리스트를 정수형 리스트로 변환
    # return list(map(int, answer))
    
    return answer