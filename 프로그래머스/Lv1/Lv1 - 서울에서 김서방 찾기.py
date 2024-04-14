def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            # f-string: f'문자열 {변수} 문자열'
            return f"김서방은 {i}에 있다"