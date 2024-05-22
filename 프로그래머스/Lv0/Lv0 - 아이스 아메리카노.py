def solution(money):
    result = []
    ice = 5500
    result.append(money // ice)
    result.append(money - result[0] * ice )


    return result