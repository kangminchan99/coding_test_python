def solution(arr, queries):

    for querie in queries:
#   이중 리스트 구조에서 queries 순서에 맞게 값 할당  
        start, end, k = querie
        for i in range(start, end + 1):
            if i % k == 0:
                arr[i] += 1
    return arr