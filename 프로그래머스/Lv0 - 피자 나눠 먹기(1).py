import math

def solution(n):
    answer = 0
    # math.ceil - 소수점 이하를 올림하여 정수로 반환
    answer =  1 if n <= 7 else math.ceil(n / 7)
    return answer