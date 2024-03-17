def solution(number, n, m):
#     &&가 아니라 &하나 쓰거나 and라고 써야됨
    if (number % n == 0 and number % m == 0):
        return 1
    else:
        return 0