def solution(myString):
    answer = []
    sum = 0
    for i in myString:

        if i == 'x':
            answer.append(sum)
            sum = 0
        else:
            sum += 1
            
    
#   마지막 요소가 x면 0을 추가하고 아니면 sum값 넣어주기
    if myString[-1] == 'x':
        answer.append(0)
    else:
        answer.append(sum)
        
    return answer