def solution(rank, attendance):
    a = list(zip(rank, attendance))
    answer = []
    answer1 = []
    for i in range(len(rank)):
        if a[i][1] == True:
            answer.append(a[i][0])
            
    b = sorted(answer)
    
    
    for j in range(len(b)):
        if len(b) > 3:
            b.pop()
            
            
    c = list(enumerate(rank))
    
    for i in range(len(b)):
        for j in range(len(c)):
            if b[i] == c[j][1]:
                answer1.append(c[j][0])

                
    
    d = (10000 * answer1[0]) + (100 * answer1[1]) + answer1[2]
    
    return d
        