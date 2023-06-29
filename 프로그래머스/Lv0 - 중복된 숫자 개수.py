def solution(array, n):
    sum = 0
    for a in array:
        if n == a:
            sum += 1
    return sum