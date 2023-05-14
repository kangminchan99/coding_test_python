import math

# 시, 분으로 나와있는걸 ex) 06:00 을 360으로 변환
def convert(time):
    # hh, mm으로 스플릿
    hh, mm = time.split(':')
    return int(hh) * 60 + int(mm)

def solution(fees, records):
    # intime(key, value)을 맵형태로 구현
    intime = {}
    # result(key, value)을 맵형태로 구현
    result = {}
    answer = []

    # 리스트 분리
    for r in records:
        # "05:34 5961 IN" 이렇게 들어오는걸 스플릿으로 나눠 앞부터 지정 ex) 05:34 = time
        time, num, inout = r.split()
        if inout == 'IN':
            # IN이면 intime에 넣어준다.
            intime[num] = convert(time)
            if num not in result:
                # result에 기록이 없으면 result 딕셔너리에 넣어주고 초기값을 0으로한다.
                result[num] = 0
        else:
            result[num] += convert(time) - intime[num]
            # 나간 기록을 계산한 뒤 intime 딕셔너리에서 삭제
            del intime[num]


    # del intime[num]해도 남아있는건 23:59로 처리하기로 했으므로 아래와 같이 계산
    for key, value in intime.items():
        result[key] += 23 * 60 + 59 - value


    # 정렬후 총 주차시간이 기본시간이하면 기본요금만 넣어준다.
    for key, value in sorted(result.items()):
        if value <= fees[0]:
            answer.append(fees[1])

        # 아니라면 기본요금 + 추가시간
        else:
            answer.append(fees[1] + math.ceil((value - fees[0])/ fees[2]) * fees[3])


    return answer