# 동적 계획법
def solution(n):
    count = 0
    # n이 0이 될때까지 실행
    while n:
        #
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            count += 1
    return count
        
        