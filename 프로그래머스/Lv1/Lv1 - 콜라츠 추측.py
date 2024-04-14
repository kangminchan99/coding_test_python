def solution(num):
    cnt = 0
#   num 1이 아닐 때 까지 실행   
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1
        
        cnt += 1
        
        if cnt >= 500:
            return -1
            
    return cnt if cnt != 0 else 0