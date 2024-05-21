def solution(n, t):
    cnt = n
    for i in range(1, t + 1):
        cnt = cnt * 2
    return cnt
        