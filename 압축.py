def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # 알파벳을 키, 1부터 26까지의 값을 값으로 하는 딕셔너리 d를 생성.
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    # while문을 이용해, 주어진 문자열이 딕셔너리 d에 있을 때까지 반복
    while True:
        if msg in d:
            answer.append(d[msg])
            break
        # 주어진 문자열을 한 글자씩 확인하면서, 딕셔너리 d에 없는 가장 긴 문자열을 찾아내어
        # 그 문자열의 직전까지의 값을 answer 리스트에 추가하고,
        #  그 문자열을 딕셔너리 d에 추가. 그리고 남은 문자열을 다시 처리하기 위해 msg를 갱신합니다.
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer