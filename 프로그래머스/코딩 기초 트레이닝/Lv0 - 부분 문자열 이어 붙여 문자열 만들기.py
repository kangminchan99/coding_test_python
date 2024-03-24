def solution(my_strings, parts):
    answer = []
    for i in range(len(my_strings)):
        detachStr = my_strings[i]
        answer.append(detachStr[parts[i][0]:parts[i][1] + 1])
    return ''.join(answer)
        