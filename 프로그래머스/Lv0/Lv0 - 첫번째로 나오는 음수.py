def solution(num_list):
    while num_list:
#        정수 앞엔 range사용
        for i in range(len(num_list)):
            if (num_list[i] < 0):
                return i
                break
        return -1