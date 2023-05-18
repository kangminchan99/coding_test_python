# 균형잡힌 괄호 찾기
def parse(str):
    correct = True
    # 열린괄호
    left = 0
    # 닫힌 괄호
    right = 0
    mystack = []
    
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            mystack.append('(')
        else:
            right += 1
            # 쌍이 안맞는경우
            if len(mystack) == 0:
                correct = False
            else:
                mystack.pop()
                
        if left == right:
            return i + 1, correct
    
    return 0, False

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if len(p) == 0:
        return p
    
    pos, correct = parse(p)
    u = p[:pos]
    v = p[pos:]
    
    if correct:
        return u + solution(v)
    
    
    answer = '(' + solution(v) + ')'
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('
    