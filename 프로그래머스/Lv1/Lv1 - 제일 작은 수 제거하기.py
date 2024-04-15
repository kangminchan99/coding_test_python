def solution(arr):
    arr1 = sorted(arr)
    
    result = []
    
    for i in range(len(arr)):
        if (arr[i] != arr1[0]):
            result.append(arr[i])
            
    return result
