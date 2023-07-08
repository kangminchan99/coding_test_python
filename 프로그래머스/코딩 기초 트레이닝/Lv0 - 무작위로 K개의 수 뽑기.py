def solution(arr, k):
    newArr = []
    
    for i in arr:
        if i not in newArr:
            newArr.append(i)
            if len(newArr) > k:
                newArr.pop()

    while len(newArr) < k:
        newArr.append(-1)
        
    return newArr