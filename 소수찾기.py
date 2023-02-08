from itertools import permutations
def solution(numbers):
    prime_set = set()

    # 1. 모든 숫자 조합을 만든다.
    for i in range(len(numbers)):
        # numbers란 스트링값을 리스트로 받으면 각각 따로 분리되어 보여진다.
        # 순열은 순서를 고려하기 때문에 파이썬에서 제공하는 permutations를 사용하면 편하다.
        # i + 1 은 조합의 개수를 말한다.
        per_list = permutations(list(numbers), i + 1)
        # 맵이라는 함수를 사용하여 하나로 엮어준다.
        # per_list이 가지고있는 4가지의 조합에 "".join함
        # 수(str.join)를 똑같이 적용시켜준다.
        # print(list(map("".join, per_list))) 
        # int형의로 변환
        # print(list(map(int, map("".join, per_list))))
        per_list = (map(int, map("".join, per_list)))
        # |=  eq)x = x | y, 중복을 제거하기 위해 집합인 set를 사용
        prime_set |=set(per_list)

    print(prime_set)
    # 2. 소수가 아닌 수 0과 1을 prime_set에서 제외
    prime_set -= set(range(0,2))
    # 에라토스테네스의 체를 사용(prime_set의 최댓값에 루트를 씌우고, 
    # range의 두번째 인자로 사용하기 위해서 1을 더해준다. 
    # int형으로 형변환(캐스팅)을 해준다.)
    lim = int(max(prime_set) ** 0.5) + 1
    for i in range(2, lim):
        # i*2 부터  max(prime_set)까지 i 간격 만큼 건너뛰면서   
        prime_set -= set(range(i*2, max(prime_set) +1, i))

    return len(prime_set)

print(solution("17"))

# # 1. prime_set을 정의
# prime_set = set()

# def isPrime(number):
#     # 6. 0과 1은 제외
#     if number in (0,1):
#         return False
#     # 7. 에라토스 테네스 체
#     lim = int(number ** 0.5 + 1)
#     for i in range(2, lim):
#         if number % i == 0:
#             return False
#     return True

# def recursive(combination, others):
#     # 5. 탈출 조건 / 비교 조건 : 지금까지 만들어진 조합을 
#     if combination != "":
#         if isPrime(int(combination)):
#             prime_set.add(int(combination))

#     # 4. 현재까지 만들어진 숫자에, 남아있는 숫자 중 하나를 더해준다.
#     for i in range(len(others)):
#         recursive(combination + others[i], others[:i] + others[i + 1:])  

# def solution(numbers):
#     # 2. 모든 조합을 만드는 recursive를 수행한다.
#     # recursive 첫번째에는 빈 스트링을 넘기고, 두번째 인자에는 numbers 전체를 넘긴다.
#     recursive("", numbers)

#     # 3. prime_set의 length를 반환한다.
#     return len(prime_set)

# print(solution("17"))






