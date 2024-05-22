def solution(numbers, direction):
    lenN = len(numbers)
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        for i in range(lenN - 1):
            answer.append(numbers[i])
    else:
        for i in range(1 , lenN):
            answer.append(numbers[i])
            
        answer.append(numbers[0])
            
    return answer
        