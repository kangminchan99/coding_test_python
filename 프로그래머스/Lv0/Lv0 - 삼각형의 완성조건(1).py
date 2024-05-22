def solution(sides):
    a = sorted(sides)
    if a[0] + a[1] > a[2]:
        return 1
    else:
        return 2