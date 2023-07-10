def solution(arr):
    stk = []
    a = len(arr)
    for i in range(a):
        if len(stk) == 0:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                stk.pop()
            else:
                stk.append(arr[i])
    
    if len(stk) == 0:
        stk.append(-1)
    return stk