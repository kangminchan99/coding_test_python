def solution(my_string, index_list):
    answer = []
    for i in index_list:
        answer.append(my_string[i])
        
    
#     ''을 없애고 리스트에 있는 문자를 하나로 합친다.
    return ''.join(answer)