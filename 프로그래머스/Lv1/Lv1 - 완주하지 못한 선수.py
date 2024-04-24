def solution(participant, completion):
    dicP = {}
    
    for i in participant:
        if i not in dicP:
            dicP[i] = 1
        else:
            dicP[i] += 1
    
    for i in completion:
        if i in dicP:
            dicP[i] -= 1
            
    
    for key, value in dicP.items():
        if value == 1:
            return key