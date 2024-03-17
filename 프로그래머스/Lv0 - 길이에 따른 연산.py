def solution(num_list):
#   길이를 반환
    lent = len(num_list)
    sum = 0
    sum1 = 1
    if (lent > 10):
        for i in num_list:
            sum += i
        return sum
    else:
        for i in num_list:
            sum1 *= i 
        return sum1