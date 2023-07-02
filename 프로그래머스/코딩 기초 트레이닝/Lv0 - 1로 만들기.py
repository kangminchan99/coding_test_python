def solution(num_list):
    sum = 0
    for i in num_list:
        # i가 1보다 크면 계속 반복
        while i > 1:
            if i % 2 == 0:
                i = i / 2
                sum += 1
            # 홀수일 때
            else:
                i = (i - 1) / 2
                sum += 1
    return sum
                    