def match(arr, key,rot, r,c):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if rot == 0:
                arr[r + i][c + j] += key[i][j]
            # 시계방향으로 90도 회전
            elif rot == 1:
                arr[r + i][c + j] += key[n-1 -j][i]
            # 180
            elif rot == 2:
                arr[r + i][c + j] += key[n-1 -i][n-1 -j]
                
            else:
                arr[r + i][c + j] += key[j][n-1 -i]
                

def check(arr, offset ,n):
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] != 1:
                return False
    return True


def solution(key, lock):
    # key와 Lock이 최소 1개는 겹쳐야 된다.
    offset = len(key) - 1
    
    # 행의 마지막 위치가 offset위치에서 자물쇠의 길이만큼 더한 값이다
    for r in range(offset + len(lock)):
        for c in range(offset + len(lock)):
            # 시계 방향으로 key돌리기
            for rot in range(4):
                # 2차원 배열 초기값 0
                arr = [[0 for _ in range(58)] for _ in range(58)]
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]
                        
                        
                match(arr, key, rot, r, c)
                if check(arr, offset, len(lock)):
                    return True
    
    # 끝까지 맞은게 없으면 False반환
    return False