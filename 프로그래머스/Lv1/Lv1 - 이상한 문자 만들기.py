def solution(s):
    s1 = s.split(' ')
    result = []
    for i in range(len(s1)):
        if i != 0:
            result.append(' ') 
        for j in range(len(s1[i])):
            if j % 2 == 0:
                result.append(s1[i][j].upper())
                continue
            else:
                result.append(s1[i][j].lower())
        
    return ''.join(result)