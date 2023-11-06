def solution(n, left, right):
    #   012
    # 0 012
    # 1 345
    # 2 678
    
    answer = []
    # left부터 right까지 반복
    for idx in range(left, right + 1):
        # row - 몫, col - 나머지
        row, col = idx // n, idx % n
        # 행과 열중 큰값 + 1
        answer.append(max(row, col) + 1)
    return answer