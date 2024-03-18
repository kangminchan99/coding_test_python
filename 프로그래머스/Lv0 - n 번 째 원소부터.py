def solution(num_list, n):
#   [n:]으로 설정 시 [3:]으로 가정하면 list는 0부터 시작하므로 -1을 해줘야 결과값이 나온다.
    a = num_list[n - 1:]
    return a
        