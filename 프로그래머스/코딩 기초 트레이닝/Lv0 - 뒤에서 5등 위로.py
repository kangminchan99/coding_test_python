def solution(num_list):
#     버블 정렬 사용
    for i in range(len(num_list) - 1, 0, -1):
        for j in range(i):
            save = 0
            if num_list[j] > num_list[j + 1]:
                save = num_list[j + 1]
                num_list[j + 1] = num_list[j]
                num_list[j] = save        
            
    
    return num_list[5:]