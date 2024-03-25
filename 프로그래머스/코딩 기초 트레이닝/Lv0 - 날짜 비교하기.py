def solution(date1, date2):
    date11 = ''.join(map(str, date1))
    date22 = ''.join(map(str ,date2))

    
    if int(date11) < int(date22):
        return 1
    else:
        return 0