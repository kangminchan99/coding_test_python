def solution(my_string, num1, num2):
    lenStr = len(my_string)
    answer = ''
    for i in range(lenStr):
        if i == num1:
            answer += my_string[num2]
            continue
        if i == num2:
            answer += my_string[num1]
            continue
        
        answer += my_string[i]
        
    return answer
        