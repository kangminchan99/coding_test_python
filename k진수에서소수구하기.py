import math

# 변환하기 위한 함수
def convert(num, base):
    # 몫과 나머지 구하기
    q, r = divmod(num, base)
    # 재귀 호출을 통해 구현
    if q:
        return convert(q, base) + str(r)
    # 몫이 0인경우
    else:
        return str(r)
    
def check(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    # 10진수일경우 입력을 받은 n을 바로 문자열로 변환
    numstr = str(n) if k == 10 else convert(n,k)
    nums = numstr.split('0')
    answer = 0
    for value in nums:
        # len(value) - 00이 두번오는 경우 제거
        if len(value) and check(int(value)):
            answer += 1
    # 진법 변환
    return answer