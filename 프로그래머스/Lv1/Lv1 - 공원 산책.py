def solution(park, routes):
    block = []
#   공원 행 길이
    rowPark = len(park)
#   공원 열 길이
    colPark = len(park[0])
    
#   장애물, 시작 위치
    for i in range(rowPark):
        for j in range(colPark):
            if park[i][j] == "X":
                block.append([i, j])
            if park[i][j] == "S":
                H = i
                W = j
                   
#   가는길
    for i in routes:
        info = i.split()
        position = info[0] 
        distance = int(info[1])
        moveNorth = H - distance
        moveEast = W + distance
        moveSouth = H + distance
        moveWest = W - distance

        if position == "N" :
            if moveNorth < 0 :
                continue
            isHuddle = 0
            for j in block :
                if j[1] == W :
                    if moveNorth <= j[0] and H > j[0] :
                        isHuddle = 1
                        break
            if isHuddle == 1 :
                continue
            H = moveNorth
        if position == "S" :
            if moveSouth > rowPark - 1 :
                continue
            isHuddle = 0
            for j in block :
                if j[1] == W :
                    if moveSouth >= j[0] and H < j[0] :
                        isHuddle = 1
                        break
            if isHuddle == 1 :
                continue
            H = moveSouth
        if position == "W" :
            if moveWest < 0 :
                continue
            isHuddle = 0
            for j in block :
                if j[0] == H :
                    if moveWest <= j[1] and W > j[1] :
                        isHuddle = 1
                        break
            if isHuddle == 1 :
                continue
            W = moveWest
        if position == "E" :
            if moveEast > colPark - 1 :
                continue
            isHuddle = 0
            for j in block :
                if j[0] == H :
                    if moveEast >= j[1] and W < j[1] :
                        isHuddle = 1
                        break
            if isHuddle == 1 :
                continue
            W = moveEast
    
    return [H, W]
                
            