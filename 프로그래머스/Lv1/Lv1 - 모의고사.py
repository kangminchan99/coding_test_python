def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    result = [0, 0, 0]
    answer = []
    
    lenAns = len(answers)
    lenP1 = len(p1)
    lenP2 = len(p2)
    lenP3 = len(p3)
    
    for i in range(lenAns):
        if answers[i] == p1[i % lenP1]:
            result[0] +=1  
        if answers[i] == p2[i % lenP2]:
            result[1] +=1 
        if answers[i] == p3[i % lenP3]:
            result[2] +=1 

    maxResult = max(result)
    for i in range(3) :
        if maxResult == result[i] :
            answer.append(i+1)

    return answer
        