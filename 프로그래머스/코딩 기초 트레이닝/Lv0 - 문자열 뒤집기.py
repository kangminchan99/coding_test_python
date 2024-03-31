def solution(my_string, s, e):

    answer = []
    
    if s != 0:
        answer.append(my_string[:s])
        answer.append(my_string[e: s-1: -1])
        answer.append(my_string[e + 1:])
#  s가 0일 때 예외처리를 안해줬음
    else:
        answer.append(my_string[e::-1])
        answer.append(my_string[e+1:])
        
        
    return ''.join(answer)