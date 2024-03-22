def solution(myString):
    answer = []
    for i in myString:
        if i < 'l':
            answer.append('l')
        else:
            answer.append(i)
    return ''.join(answer)