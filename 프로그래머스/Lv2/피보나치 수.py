def solution(n):
    # 피보나치 수열
    # F(2) = F(0) + F(1) = 0 + 1 = 1
    # F(3) = F(1) + F(2) = 1 + 1 = 2
    # F(4) = F(2) + F(3) = 1 + 2 = 3
    # F(5) = F(3) + F(4) = 2 + 3 = 5

    # F(0), F(1)
    a, b = 0, 1 
    for i in range(n):
#      피보나치 수열: a = b, b = a + b
        a, b = b, a + b
    return a % 1234567