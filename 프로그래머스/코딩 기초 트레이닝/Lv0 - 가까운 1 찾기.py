def solution(arr, idx):
    answer = []
#   range(len(arr)):   
    for i in range(len(arr)):
        if arr[i] == 1 and i >= idx:
            answer.append(i)
            
    return answer[0] if len(answer) > 0 else -1