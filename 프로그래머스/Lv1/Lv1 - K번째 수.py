def solution(array, commands):
    result = []
    for i in commands:
        start , end, idx = i
        change = array[start - 1:end]
        srtChange = sorted(change)
        result.append(srtChange[idx - 1])
        
    return result
        