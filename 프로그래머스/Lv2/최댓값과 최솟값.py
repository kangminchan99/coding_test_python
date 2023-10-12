def solution(s):
    # s를 공백으로 분리해주고 int로 변환하여 list만들어주기
    numbers = list(map(int, s.split()))
    # 최솟값
    min_num = min(numbers)
    # 최댓값
    max_num = max(numbers)
    return str(min_num) + ' ' + str(max_num)
    