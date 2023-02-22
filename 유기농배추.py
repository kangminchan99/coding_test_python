# # visted 배열을 활용한 풀이
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# MAX = 50 + 10

# # row, column: (1,0) - 아래로 한칸, (-1,0) - 위로 한칸, (0,1) - 오른쪽, [0,-1] - 왼쪽
# dirR = [1, -1, 0, 0]
# dirC = [0, 0, 1, -1]

# def dfs(y,x):
#     global visited
#     visited[y][x] = True
#     for dirIdx in range(4):
#         newY = y + dirR[dirIdx]
#         newX = x + dirC[dirIdx]
#         if graph[newY][newX] and not visited[newY][newX]:
#             dfs(newY,newX)

# # 0. 입력 및 초기화
# TestCase = int(input())
# for _ in range(TestCase):
#     M, N, K = map(int(input().split()))
#     # 그래프는 False되었고 MAX개가 있는데, 그 행이 MAX개가 있다.
#     graph = [[False] * MAX for _ in range(MAX)] 
#     visited = [[False] * MAX for _ in range(MAX)] 
#     # 1. 그래프 정보 입력
#     for _ in range(K):
#         x, y = map(int(input().split()))
#         # 그래프의 0,0 베이스를 1,1베이스로 변경
#         graph[y + 1][x + 1] = True
#     # 2. 방문하지 않은 지점부터 dfs 돌기
#     answer = 0
#     for i in range(1, N + 1):
#         for j in range(1, M + 1):
#             # 만약 그래프 i,j에 배추가 있고 방문한 적이 없으면 dfs의 i,j를 불러준다.
#             if graph[i][j] and not visited[i][j]:
#                 dfs(i,j)
#                 answer += 1
#     print(answer)


# graph배열만 활용한 풀이
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50 + 10

# row, column: (1,0) - 아래로 한칸, (-1,0) - 위로 한칸, (0,1) - 오른쪽, [0,-1] - 왼쪽
dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]

def dfs(y,x):
    graph[y][x] = False
    for dirIdx in range(4):
        newY = y + dirR[dirIdx]
        newX = x + dirC[dirIdx]
        if graph[newY][newX]:
            dfs(newY,newX)

# 0. 입력 및 초기화
TestCase = int(input())
for _ in range(TestCase):
    M, N, K = map(int(input().split()))
    # 그래프는 False되었고 MAX개가 있는데, 그 행이 MAX개가 있다.
    graph = [[False] * MAX for _ in range(MAX)] 
    # 1. 그래프 정보 입력
    for _ in range(K):
        x, y = map(int(input().split()))
        # 그래프의 0,0 베이스를 1,1베이스로 변경
        graph[y + 1][x + 1] = True
    # 2. 방문하지 않은 지점부터 dfs 돌기
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # 만약 그래프 i,j에 배추가 있고 방문한 적이 없으면 dfs의 i,j를 불러준다.
            if graph[i][j]:
                dfs(i,j)
                answer += 1
    print(answer)


