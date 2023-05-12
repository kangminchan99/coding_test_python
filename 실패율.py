from functools import cmp_to_key

def compare(a,b):
    if a[1] == b[1]:
        return a[0] - b[0]
    return b[1] - a[1]

def solution(N, stages):
    answer = []
    # 사람 수는 len(stages)와 같다
    total  = len(stages)
    fails = []
    # 각각의 스테이지에 몇명의 사람이 있는지 넣어두기
    # 초기값 0
    users = [0 for _ in range(N+1)]
    for stage in stages:
        # index를 0부터 쓰기위해서 1빼고 시작
        users[stage - 1 ] += 1
        
    for i in range(N):
        if users[i] == 0:
            fails.append((i+1, 0))
        else:
            fails.append((i+1,users[i]/total))
            total -= users[i]
            
    for f in sorted(fails, key = cmp_to_key(compare)):
        answer.append(f[0])
    
    return answer
    
    