def solution(arr, n):
    arrlen = len(arr)
    if arrlen % 2 == 0:
#       1부터 arr의 길이만큼 i를 2씩 증가해서
        for i in range(1, arrlen, 2):
            arr[i] += n
    else:
#       반복문 범위 지정하기 range(초기, 끝, 증가)
        for i in range(0, arrlen, 2):
            arr[i] += n
            
    return arr