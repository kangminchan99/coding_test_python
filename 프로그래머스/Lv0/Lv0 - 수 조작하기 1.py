def solution(n, control):
    plus = n
    # 딕셔너리 사용
    dic = {'w': 1 , 's' : -1, 'd': 10, 'a': -10}
    
    for i in control:
        plus += dic[i]
    return plus