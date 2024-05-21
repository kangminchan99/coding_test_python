def solution(n):
    pizza = 6
    cnt = 0
    while True:
        if pizza % n == 0:
            cnt += 1
            return cnt
        else:
            pizza += 6
            cnt += 1
            continue 

            
            