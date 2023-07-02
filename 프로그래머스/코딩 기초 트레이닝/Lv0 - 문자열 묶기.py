def solution(strArr):
    dic = {}
    count = 0
    for i in strArr:
        a = len(i)
        if a not in dic:
            dic[a] = []
            dic[a].append(i)
        else:
            dic[a].append(i)
            
    for i, j in dic.items():
        if len(j) > count:
            count = len(j)
    return count