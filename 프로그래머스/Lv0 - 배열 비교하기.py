def solution(arr1, arr2):
    a1 = len(arr1)
    a2 = len(arr2)
    a1sum = sum(arr1)
    a2sum = sum(arr2)

#    길이가 같고 합이 다를 경우를 추가해줘야됨
    if (a2 == a1 and a1sum == a2sum):
        return 0
    elif (a1 == a2 and a1sum > a2sum):
        return 1
    elif (a1 == a2 and a2sum > a1sum):
        return -1
    elif (a1 > a2):
        return  1
    else:
        return -1