def solution(arr):
    answer = []
    for i in arr:
        answer.append([i] * i)
#   이중 리스트 평탄화하기
    return sum(answer, [])