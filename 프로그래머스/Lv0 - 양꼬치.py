def solution(n, k):
    answer = 0
    serv = n // 10
    answer = n * 12000 + (k - serv) * 2000
    return answer