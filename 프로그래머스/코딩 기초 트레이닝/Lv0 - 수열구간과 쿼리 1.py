def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
#       이거 문제가 [s, e]사이의 범위를 전부 1씩 증가시켜주는건데 문제를 제대로 안읽었음....
        for j in range(queries[i][0], queries[i][1] + 1):
            arr[j] += 1
    return arr
        