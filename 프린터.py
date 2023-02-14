def solution(priorities, location):
    # 큐(Queue)에서 하나씩 꺼내서 수행할 수 있으면 하고 아니면 다시 넣는다.
    # enumerate - 각각의 인덱스를 붙여줘 튜플로 관리

    # priorities에서 하니씩 꺼내온 인덱스를 a에 넣고 실제값을 b에 넣는다.
    Queue = [(a,b) for a,b in enumerate(priorities)]
    answer = 0
    while Queue:
        i = Queue.pop(0)
        # 우선순위를 가져오기 위해 1번 인덱스를 가져온다.
        # i에서 하나씩 꺼내온것이 우선순위가 현재 i보다 높은 것이 있으면, any문은 true가 된다.
        if any(i[1] < other_i[1] for other_i in Queue):
            Queue.append(i)
        else:
            answer += 1
            # location이 현재와 같으면 브레이크
            if i[0] == location:
                break
    return answer
print(solution([2,1,3,2],1))