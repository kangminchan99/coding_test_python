def solution(numbers):
    answer = 0
    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    
    for i in numbers:
        if i in dic:
            dic[i] += 1
            
    for key, item in dic.items():
        if item == 0:
            answer += key
            
    return answer