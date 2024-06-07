def solution(keyinput, board):
    maxX = board[0] // 2
    minX = -(board[0] // 2)
    maxY = board[1] // 2
    minY = -(board[1] // 2)
    
    result = [0, 0]
    dic = {'right': 1, 'left': -1, 'up': 1, 'down': -1}
    lenKey = len(keyinput)
    for i in range(lenKey):
        if keyinput[i] == 'right' or keyinput[i] == 'left':
            result[0] += dic[keyinput[i]]
        else:
            result[1] += dic[keyinput[i]]
    
    if result[0] > maxX:
        result[0] = maxX
    elif result[0] < minX:
        result[0] = minX
    
    if result[1] > maxY:
        result[1] = maxY
    elif result[1] < minY:
        result[1] = minY
        
    return result
            
            
            