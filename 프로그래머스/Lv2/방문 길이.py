def solution(dirs):
    # 처음 지나가 본 길의 길이가 필요하므로 중복을 제거하기 위한 set()변수 sets설정
    sets = set()
    y, x = 0, 0
    dic = {'U': (1,0), 'D': (-1,0),'R': (0,1),'L': (0,-1)}
    
    # dirs문자열을 하나씩 순회하면서 이동 방향에 따라 ny, nx를 계산
    for d in dirs:
        dy, dx = dic[d]
        ny = y + dy
        nx = x + dx
        # 유효한 좌표 범위에 있으면
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            # 
            sets.add(((y,x), (ny, nx)))
            sets.add(((ny,nx), (y, x)))
            y = ny
            x = nx

    return len(sets) // 2