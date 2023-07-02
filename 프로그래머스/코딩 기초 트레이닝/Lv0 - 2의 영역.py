def solution(arr):
    result = []
    answer = []
    
    # 리스트 형태로 arr배열에 순서를 지정해주고 
    a = list(enumerate(arr))
    # arr길이만큼 돌아가면서 2찾기
    for i in range(len(arr)):
        if a[i][1] == 2:
            result.append(a[i][0])
    if len(result) > 1:
        first = result[0]
        last = result[-1]
        answer = arr[first:last+1]
                
    elif len(result) == 1:
        answer.append(2)
    else:
        answer.append(-1)
                    
                    
                
    return answer
    