def solution(str_list, ex):
    answer = []
    for i in range(len(str_list)):
#       ex가 str_list[i]에 없을 경우  
        if ex not in str_list[i]:
            answer.append(str_list[i])
    
#   리스트 안의 문자열을 한개의 문자열을 합칠라면 ''.join()
#   을 사용한다.
    return ''.join(answer)