def solution(A, B):
    # 오름차순
    a = sorted(A)
    # 내림차순
    b = sorted(B, reverse = True)
    sum = 0
    
    for i in range(len(a)):
        sum += a[i] * b[i]
            
    return sum