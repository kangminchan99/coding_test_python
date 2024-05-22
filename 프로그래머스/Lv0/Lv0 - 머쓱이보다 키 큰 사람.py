def solution(array, height):
    sum = 0
    for a in array:
        if a > height:
            sum += 1
    return sum