def solution(l, r):
    answer = []
    for i in range(l, r + 1):
#       if (all(num in ['0', '5'] for num in str(i))) --> 0하고 5만 들어있는 str(i)를 찾는다 
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
            
    if answer == []:
        answer.append(-1)

    return answer

                
    
