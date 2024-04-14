def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
             answer.append(i)
    
    if len(answer) != 0:
#       원본 변경 x
        return sorted(answer)
    else:
        return [-1]