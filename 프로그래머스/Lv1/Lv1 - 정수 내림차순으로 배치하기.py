def solution(n):
    answer = []
    for i in str(n):
        answer.append(i)
#   내림차순 정렬 sorted(list, reverse=True)
    result = sorted(answer ,reverse=True)
    
    return int(''.join(result))