def solution(board, h, w):
    answer = 0
    lenBoard = len(board)
    
#   h가 마지막이 아닐 때
    if h < lenBoard - 1 and board[h + 1][w] == board[h][w]:
        answer += 1
    
#   h가 0번째가 아닐 때 
    if h > 0 and board[h - 1][w] == board[h][w]:
        answer += 1
        
#   w가 0번째가 아닐 때
    if w > 0 and board[h][w - 1] == board[h][w]:
        answer += 1
        
#   w가 마지막이 아닐 때
    if w < lenBoard - 1 and board[h][w + 1] == board[h][w]:
        answer += 1
        
    return answer
            