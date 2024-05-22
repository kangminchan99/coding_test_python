def solution(array):
    maxA = max(array)
    answer = [maxA]
    
    for i in range(len(array)):
        if array[i] == maxA:
            answer.append(i)
            
    return answer
            