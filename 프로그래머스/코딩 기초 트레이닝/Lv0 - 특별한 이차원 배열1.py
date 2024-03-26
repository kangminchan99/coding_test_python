def solution(n):
    # n by n 크기의 0으로 초기화된 2차원 리스트 생성
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(len(result)):
#       [i][i] 번째 값을 1로 바꿔준다.
        result[i][i] = 1
        
    return result 