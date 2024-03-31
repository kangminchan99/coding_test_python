def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                return 0
#   전체가 같아야 1리턴 이구나 ㅅㅂ
    return 1