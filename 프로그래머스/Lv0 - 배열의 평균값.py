def solution(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum / len(numbers)