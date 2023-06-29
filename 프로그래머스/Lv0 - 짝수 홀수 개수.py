def solution(num_list):
    answer = []
    even = 0
    odd = 0
    for n in num_list:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    answer.insert(0, even)
    answer.insert(1, odd)
    
    return answer