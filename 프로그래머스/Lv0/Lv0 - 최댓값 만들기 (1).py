def solution(numbers):
    first = max(numbers)
    
    for i, v in enumerate(numbers):
        if v == first:
            del numbers[i]
            break
    
    second = max(numbers)
    
    return first * second
        