def solution(A, B):
    cnt = 0
    
    for i in range (len(A)) :
        if A == B:
            return cnt 
        else:
            cnt += 1
            change = A[-1]
            A = change + A[0 : -1]
            
    return -1