def solution(myString, pat):
    answer = []
    for i in range(len(myString)):
        if myString[i] == 'A':
            answer.append('B')
        else:
            answer.append('A')
            
    sumList = ''.join(answer)
    
    if pat in sumList:
        return 1
    else:
        return 0