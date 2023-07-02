def solution(myString, pat):
    a = list(enumerate(myString))
    answer = []
    for i, j  in a:
        if j == pat[-1]:
            answer.append(myString[:i+1])
    
    return answer[-1]