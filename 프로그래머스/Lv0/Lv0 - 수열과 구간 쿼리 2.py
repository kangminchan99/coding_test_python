def solution(arr, queries):
    answer = []
    for i, j, k in queries:
        check = 10000001
        for s in arr[i:j+1]:
            if s > k and check > s:
                check = s
        
        if check == 10000001:
            answer.append(-1)
        else:
            answer.append(check)
        
    return answer