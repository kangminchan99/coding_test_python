def solution(numbers):
    sortN = sorted(numbers, reverse = True)
    maxPosi = sortN[0] * sortN[1]
    maxNega = sortN[-1] * sortN[-2]
    if maxPosi > maxNega:
        return maxPosi
    else:
        return maxNega