import math

def solution(progresses, speeds):
    lenS = len(speeds)
    answer = []
    cnt = 1
    for i in range(lenS):
        answer.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    checked = answer[0]
    result = []
    for i in answer[1:]:
        if i > checked:
            result.append(cnt)
            checked = i
            cnt = 1
        else:
            cnt += 1
    result.append(cnt)
            
    return result
