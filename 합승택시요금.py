# 어디까지 합승할지가 관건, 모든 경로에서 둘의 합승 위치를 정한다음 최솟값을 비교한다(완전탐색) - 합승요금, a추가요금, b추가 요금.



def floyd(dist, n):
    # 경유지
    for k in range(n):
        # 출발지
        for i in range(n):
            # 도착지
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


#Floyd-warshall 알고리즘 - 모든 최단 경로를 구하는 알고리즘
def solution(n, s, a, b, fares):
    # 모든지점까지의 최단경로

    INF = 40000000
    # 초기값은 이론상 무한대. n값은 입력받은 지점
    dist = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for edge in fares:
        dist[edge[0]-1][edge[1]-1] = edge[2]
        dist[edge[1]-1][edge[0]-1] = edge[2]

    floyd(dist, n)

    s -= 1
    a -= 1
    b -= 1

    answer = INF
    for k in range(n):
        answer = min(answer,dist[s][k] + dist[k][a] + dist[k][b])
    return answer
