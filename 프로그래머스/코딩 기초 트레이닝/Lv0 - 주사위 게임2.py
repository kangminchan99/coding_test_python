def solution(a, b, c):
#   3개의 주사위가 같을 경우
    if a == b and b == c and a == c:
        return (a + b + c) * (a*a + b*b + c*c ) * (a*a*a + b*b*b + c*c*c)
#   2개의 주사위가 같을 경우
    elif a == b or b == c or a == c:
        return (a + b + c) * (a*a + b*b + c*c )
#   전부 다를 경우  
    else:
        return a + b + c