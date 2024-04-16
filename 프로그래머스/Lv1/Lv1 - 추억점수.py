def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    for i in photo:
        count = 0
        for j in i:
            if j in dic:
                count += dic[j]
        answer.append(count)
                  
    return answer