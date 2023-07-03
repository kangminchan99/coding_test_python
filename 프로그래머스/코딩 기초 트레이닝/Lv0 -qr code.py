def solution(q, r, code):
    a = list(enumerate(code))
    count = ''
    for i in range(len(a)):
        if a[i][0] % q == r:
            count += a[i][1]
    return count