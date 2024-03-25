def solution(arr, intervals):
    answer = []
    a = arr[intervals[0][0]: intervals[0][1] + 1]
    b = arr[intervals[1][0]: intervals[1][1] + 1]
    
    answer.append(a)
    answer.append(b)
    
    
#   2차원 배열을 1차원으로 바꾸기
    return sum(answer, [])