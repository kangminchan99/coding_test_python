import queue

# 상,하,좌,우 정의
# 델타값 - 열을 고정하고 -1을 빼주면 위로, 1을 더하면 아래로 이동
D = ((-1,0), (1,0),(0,-1),(0,1))

# bfs에서는 큐를 이용
def bfs(place, row, col):
    # 초기값 False, 5 by 5로 정의
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = queue.Queue()
    # 시작위치는 방문했다고 마킹하고 큐에 인큐
    visited[row][col] = True
    # q에 넣어야 되는것 3개 행,열, 거리
    q.put((row, col,0))
    
    while not q.empty():
        curr = q.get()
        # 거리가 2를 초과하면 스킵
        if curr [2] > 2:
            continue
        # 거리가 2를 초과하지 않고 
        # 시작위치가 아닌 다른위치에서 'P'를 만날경우
        if curr[2] != 0 and place[curr[0]][curr[1]] == 'P':
            return False
        
        # 아직 응시자를 만나지 못한경우 상,하,좌,우를 이동하며 탐색
        for i in range(4):
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            # 범위를 벗어날 경우 스킵
            if nr < 0 or nr > 4 or nc < 0 or nc > 4:
                continue
            # visited에 이미 들어가 있는 정보라면 스킵
            if visited[nr][nc]:
                continue
            if place[nr][nc] == 'X':
                continue
            visited[nr][nc] = True
            q.put((nr,nc,curr[2] + 1))
    return True


def check(place):
    # 행과 열을 다 돌면서 응시자 찾기
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                # bfs를 돌면서 2칸 이내에 'P'를 만날경우 false반환
                if bfs(place, r, c) == False:
                    return False
            
    # 중간에 ruturn되는 경우없이 이중 for문이 끝날경우 true 반환
    return True
                
    


def solution(places):
    answer = []
    
    for place in places:
        # check라는 함수를 만들어 거리두기를 지키고 있는지 확인
        if check(place):
            # true
            answer.append(1)
        else:
            # false
            answer.append(0)
            
    return answer