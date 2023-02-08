prime_set = set()

def isPrime(number):
    # 6. 0과 1은 제외
    if number in (0,1):
        return False
    # 7. 에라토스 테네스 체
    lim = int(number **0.5 + 1)
    for i in range(2, lim):
        if number % i == 0:
            return False
    return True

def recursive(combination, others):
    # 5. 탈출 조건 / 비교 조건 : 지금까지 만들어진 조합을 
    if combination != "":
        if isPrime(int(combination)):
            prime_set.add(int(combination))

    # 4. 현재까지 만들어진 숫자에, 남아있는 숫자 중 하나를 더해준다.
    for i in range(len(others)):
        recursive(combination + others[i], others[:i] + others[i + 1:])  

def solution(numbers):
    # 2. 모든 조합을 만드는 recursive를 수행한다.
    # recursive 첫번째에는 빈 스트링을 넘기고, 두번째 인자에는 numbers 전체를 넘긴다.
    recursive("", numbers)

    # 3. prime_set의 length를 반환한다.
    return len(prime_set)

print(solution("17"))