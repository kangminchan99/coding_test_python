def solution(a, b, c, d):
    dic = {'1':0, '2':0, '3':0, '4':0 , '5':0, '6':0}
    
    answer = [a, b, c, d]
    
    for i in answer:
        if str(i) in dic:
            dic[str(i)] += 1
    
    if 4 in dic.values():
        for k, v in dic.items():
            if v == 4:
                return int(k * 4)
    
    if 3 in dic.values():
        big = 0
        small = 0
        for k, v in dic.items():
            if v == 3:
                big += int(k)
                continue
            if v == 1:
                small += int(k)
        
        return ((10 * big) + small) * ((10 * big) + small)
    
    
    if max(dic.values()) == 2 and 1 not in dic.values():
        check = ''
        for k, v in dic.items():
            if v == 2:
                check += k
        
        return (int(check[0]) + int(check[1])) * abs(int(check[0]) - int(check[1]))
    
    if max(dic.values()) == 2 and 1 in dic.values():
        check = ''
        for k, v in dic.items():
            if v == 1:
                check += k
        
        return (int(check[0]) * int(check[1]))
    
    if max(dic.values()) == 1:
        maxKey = 7
        for k, v in dic.items():
            if v == 1 and int(k) < maxKey:
                maxKey = int(k)
                
        return maxKey
            
            
        