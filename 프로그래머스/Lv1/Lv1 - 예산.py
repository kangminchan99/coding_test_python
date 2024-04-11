def solution(d, budget):
    sortList = sorted(d)
    sum = 0
    answer = []
    for i in sortList:
        if budget > sum:
            sum += i
            answer.append(i)
            
                
    return len(answer) if sum <= budget else len(answer) - 1
