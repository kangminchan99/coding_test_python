def solution(food):
    answer = []

    for i in range(1, len(food)):
#       음식 갯수가 2개이상이고 홀수인 경우
        change = 0
        if food[i] >= 2 and food[i] % 2 == 1:
            change = (food[i] - 1) // 2
        
        if food[i] >= 2 and food[i] % 2 == 0:
            change = (food[i]) // 2
            
        
        for j in range(change):
            answer.append(i)
            
    answer.append(0)
    
    for i in range(len(answer) - 2, -1, -1):
        answer.append(answer[i])

    return ''.join(str(x) for x in answer)