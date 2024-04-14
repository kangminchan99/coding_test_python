def solution(phone_number):
    phoneLen = len(phone_number)  - 4
    
    answer = []
    answer.append('*' * phoneLen)
    
    answer.append(phone_number[phoneLen:])
    
    return ''.join(answer)