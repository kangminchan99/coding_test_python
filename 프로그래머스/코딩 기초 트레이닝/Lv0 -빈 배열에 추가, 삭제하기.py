def solution(arr, flag):
    answer = []
    result = list(zip(arr, flag))
    for i in result:
        if i[1] == True:
            # answer리스트에 요소 추가
            answer.extend([i[0]] * (i[0] * 2))
        else:
            # 뒤에서 -i[0]번까지 삭제
            answer = answer[:-i[0]]
    return answer