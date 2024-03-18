def solution(num_list):
#     마지막 원소 출력
    length = len(num_list) - 1
    if (num_list[length] > num_list[length - 1]):
        num_list.append(num_list[length] - num_list[length -1])
    else:
        num_list.append(num_list[length] * 2)
        
    return num_list