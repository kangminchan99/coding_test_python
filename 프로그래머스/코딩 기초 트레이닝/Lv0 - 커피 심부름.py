def solution(order):
    count = 0 
    
    for i in order:
        if 'americano' in i:
            count += 4500
        elif 'cafelatte' in i:
            count += 5000
        else:
            count += 4500
    return count
            