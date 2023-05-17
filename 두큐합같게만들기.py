from collections import deque

def solution(queue1, queue2):
    
    n = len(queue1)
    tot1, tot2 = sum(queue1), sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)
    

    # 반복문은 4*n+1번 실행. 이는 교환 횟수가 최대로 큐1과 큐2의 모든 원소를 한 번씩 교환하고 더해지는 경우를 고려했을 때의 값입니다
    for i in range(4*n+1):
        if tot1 == tot2:
            return i
        if tot1 < tot2:
            x = q2.popleft()
            tot1 += x
            tot2 -= x
            q1.append(x)
        else:
            x = q1.popleft()
            tot2 += x
            tot1 -= x
            q2.append(x)
    return -1