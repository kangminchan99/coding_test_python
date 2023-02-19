import sys
def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            dfs[next]

def bfs():
    global q, visited
    while q:
        # 0번 인덱스를 뽑아와서 cur에 담겠다.
        cur = q.pop(0)
        print(cur, end = ' ')
        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                # q의 뒤에 이어서 붙인다.
                q.append(next)

# 0. 입력 및 초기화
input = sys.stdin.readline
N, M, V = map(int, input().split())


# False 만 (N + 1)개 가지고 있는 1차원 배열을 (N + 1)개의 행을 갖도록 구현
# (N + 1)개 * (N + 1)개의 False로 구현된 2차원 배열
graph = [[False] * (N + 1) for _ in range(N + 1)]
# 1차원 배열 하나
visited = [False] * (N + 1)
# 1. 그래프 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
# 2. dfs
dfs(V)
print()

# 3. bfs
visited = [False] * (N + 1)
q = [V]
visited[V] = True
bfs()
