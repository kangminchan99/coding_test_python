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


#--------------------------------------------------#

# def solution(dartResult):
#     answer = []
#     # i가 dartResult를 순회하면서 enumerate - 앞에 번호를 매겨준다.
#     for num,i in enumerate(dartResult, 1):
#         if i == 'S':
#             # answer[-1]번째의 1승
#             answer[-1] **= 1
#         elif i == 'D':
#             # answer[-1]번째의 2승
#             answer[-1] **= 2
#         elif i == 'T':
#             # answer[-1]번째의 3승
#             answer[-1] **= 3        
#         elif i == '*':
#             answer[-1] *= 2
#             if len(answer) >= 2:
#                 answer[-2] *=2
#         elif i == '#':
#             answer[-1] *= -1
#         else:
#             # 두개씩 슬라이싱해서 10인것과 10이 아닌것
#             if dartResult[num-1: num+1] == '10':
#                 answer.append(10)
#             elif dartResult[num-2:num] != '10':
#                 answer.append(int(i)) 

#     return sum(answer)

# print(solution('1S2D*10T'))      





# 정규표현식
# import re

# testcase = ['1S2D*3T', '1D2S#10S']


# def solution(dartResult):
#     pattern = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
#     answer = []
#     # 계산식을 딕셔너리 형태로
#     formula = {'S': lambda 값:값,'D': lambda 값:값**2,'T': lambda 값:값**3,}

#     for 숫자,승수, 상 in pattern.findall(dartResult):
#         if 승수 == 'S':
#             점수 = formula['S'](int(숫자))
#         elif 승수 == 'D':
#             점수 = formula['D'](int(숫자))
#         elif 승수 == 'T':
#             점수 = formula['T'](int(숫자))  
#         if 상 == '*':
#             점수 *= 2
#             if answer:
#                 answer[-1] *=2
#         elif 상 == '#':
#             점수 *= -1

#         answer.append(점수)

#     return sum(answer)

# print(solution('1D2S#10S')) 