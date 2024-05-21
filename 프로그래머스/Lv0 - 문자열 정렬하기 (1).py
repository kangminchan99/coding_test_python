def solution(my_string):
    answer = []
    for i in my_string:
        if i.isalpha() == False:
            answer.append(int(i))
    
    return sorted(answer)