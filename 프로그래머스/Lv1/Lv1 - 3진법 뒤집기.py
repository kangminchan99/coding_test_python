def solution(n):
    answer = []
    while n > 0:
        if n // 3 != 1: 
            answer.append(n % 3)
            n //= 3
        else:
            answer.append(n % 3)
            answer.append(n // 3)
            break

    # length = len(answer)
    # for i in range (length - 1, -1, -1) :
    #     print(answer[i])
    
    answer.reverse()
    
    count = 0
    for i in range(len(answer)):
        if i == 0:
            count += answer[i]
        else:
            count += (3 ** i) * answer[i] 
            
    return count
        
    
    
    
    
    