def solution(myString, pat):
    a = len(pat)
    answer = []
    count = 0

    # while True:
    for i in range(len(myString)):
        answer.append(myString[i:a])
        a += 1
        
    for i in answer:
        if i == pat:
            count += 1
            
    return count