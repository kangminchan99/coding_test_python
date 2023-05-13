

def convert(n, base):
    T = '0123456789ABCDEF'
    q, r = divmod(n,base)
    # 몫이 0인경우 나머지r을 T에서 찾아서 반환
    if q == 0:
        return T[r]
    # 0이 아닐경우 재귀호출하고 T의 나머지 인덱스를 붙인다.
    else:
        return convert(q,base) + T[r]
    
def solution(n, t, m, p):
    answer = ''
    allstr = ''
    
    # 0부터 9999까지의 수를 n진법으로 변환한 모든 문자열을 allstr에 더합니다.
    for i in range(100000):
        allstr += convert(i,n)
        
    # answer길이가 t보다 작으면 반복
    while len(answer) < t:
        # answer에 allstr의 튜브순서 p번째 단어를 붙인다.
        answer += allstr[p -1]
        # p에 참가인원 m을 더한다.
        p += m
    return answer