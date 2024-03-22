def solution(binomial):
    bi = binomial.split(' ')
    if bi[1] == '*':
        return int(bi[0]) * int(bi[2])
    elif bi[1] == '+':
        return int(bi[0]) + int(bi[2])
    else:
        return int(bi[0]) - int(bi[2])