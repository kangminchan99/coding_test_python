def solution(wallpaper):
    lenWall = len(wallpaper)
    answer = []
    minX = 99
    minY = 99
    maxX = 0
    maxY = 0
    for i in range(lenWall):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                answer.append([i, j])
    
    lenAnswer = len(answer)
    if lenAnswer == 1:
        sumA = sum(answer, [])
        sumA.append(answer[0][0] + 1)
        sumA.append(answer[0][1] + 1)
        return sumA
    else:
        for x, y in answer:
            if x < minX:
                minX = x
            
            if y < minY:
                minY = y
            
            if x > maxX:
                maxX = x
                
            if y > maxY:
                maxY = y
    
    return [minX, minY, maxX + 1, maxY + 1]