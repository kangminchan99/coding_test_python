def solution(numLog):
    answer = []
    dic = {1 : 'w', -1: 's', 10: 'd', -10: 'a'}
    
    for i in range(len(numLog) - 1):
        inDic = numLog[i + 1] - numLog[i]
        answer.append(dic[inDic])
        
    return ''.join(answer)