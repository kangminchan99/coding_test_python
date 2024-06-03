def solution(polynomial):
    xcnt = 0
    num = 0
    result = ''
    for i in polynomial.split():
        if 'x' == i:
            xcnt += 1
        elif 'x' in i:
            xcnt += int(i[0:-1])
        
        elif i != '+':
            num += int(i)

    if xcnt != 0 :
        if xcnt != 1 :
            result += str(xcnt)
        result += 'x'
    if num != 0 :
        if xcnt != 0 :
            result += ' + '
        result += str(num)
        
    return result
    
    

        