def solution(num, k):
    strN = str(num)
    lenN = len(strN)
    strK = str(k)

    if strK in strN:
        for i in range(lenN):
            if strN[i] == strK:
                return i + 1
    else:
        return -1