def solution(start, end_num):
    answer = []
    while True:
        # start넘버부터 계속 리스트에 넣어가면서 1씩 줄여준다
        answer.append(start)
        start -= 1
        # end_num까지 리스트에 넣어주어야 하므로 -1을 해준다.
        if (start == end_num -1):
            break
            
    return answer