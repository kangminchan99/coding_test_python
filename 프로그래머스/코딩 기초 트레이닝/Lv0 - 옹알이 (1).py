def solution(babbling):
    word = [ "aya", "ye", "woo", "ma"]
    check = ''
    result = 0
    for i in babbling:
        for j in i:
            check += j
            if check in word:
                check = ''

        if check == '':
            result += 1
        check = ''
    
    
    return result
                
                