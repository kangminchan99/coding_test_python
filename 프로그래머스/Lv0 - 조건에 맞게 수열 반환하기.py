def solution(arr, k):
    list = []
    if (k % 2 == 0):
        for i in arr:
            list.append(i + k)
    else:
        for i in arr:
            list.append(i * k)
    return list
            