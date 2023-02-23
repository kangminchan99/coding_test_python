def solution(dartResult):
    # 0. 입력 및 초기화
    scores = []
    start_idx = 0
    # 딕셔너리를 만들어줘서 영문자의 값을 지정해준다.
    power = {'S' : 1, 'D': 2, 'T': 3}    
    # 1. dartResult 별로 처리
    for i in range(len(dartResult)):
        op = dartResult[i]
        if op in power:
            # scores리스트에 dartResult의 start_idx부터 i의 전까지 인트로 변환하여 추가해준다음 승수를 올려준다.
            scores.append(int(dartResult[start_idx:i]) ** power[op])

        elif op == '*':
            # scores의 가장 뒤에 있는 2개의 값을 가져오고 그것을 2배씩 곱한 다음에 다시 배열 형태로 만들어준다음 원래 위치에 담아준다.
            scores[-2:] = [x * 2 for x in scores[-2:]]
        elif op == '#':
            # scores의 가장 마지막 인덱스를 -로 바꿔준다음 원래 위치에 넣어준다.
            scores[-1] = -scores[-1]

        # op라는 문자가 숫자가 아니라면, start_idx =  i + 1(다음위치부터 정수가 시작한다는 것을 의미)을 해준다.
        if not op.isnumeric():
            start_idx =  i + 1


    # 2. scores의 합을 반환
    return sum(scores)


solution('1S2D*3T')