def solution(num_list):
    suum = 0
    mul = 1
    for i in num_list:
        suum += i
        mul *= i
    if (mul > suum * suum):
        return 0
    else:
        return 1