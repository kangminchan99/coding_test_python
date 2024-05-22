def solution(num_list, n):
    sum = 0
    for i in num_list:
#         같은게 존재하면 sum = 1 아니면 0
        if (i == n):
            sum = 1
    return sum
            