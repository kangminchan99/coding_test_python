def solution(i, j, k):
    cnt = 0
    for v in range(i, j + 1):
        for w in str(v):
            if w == str(k):
                cnt += 1
    return cnt