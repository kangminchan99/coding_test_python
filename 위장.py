
# 해시맵 사용
def solution(clothes):
    # 1. 옷을 종류별로 구분한다.
    hashMap = {}
    # clothes의 0번째 인덱스를 cloth, 1번째 인덱스를 type으로 가져온다.
    for cloth, type in clothes:
        # 타입에 대한 해시맵을 만들어주고, 해쉬맵의 타입이 존재하는지를 본 후 타입이 가지고 있었던 value를 가져온다.
        # 0의 의미 - type이 존재하지 않는다면 초기값을 0으로 가져와라.
        hashMap[type] = hashMap.get(type, 0) + 1


    # 2. 입지 않는 경우(none)를 추가하여 모든 조합을 계산
    answer = 1
    for type in hashMap:
        answer *= hashMap[type] + 1


    # 3. 아무 종류의 옷도 입지 않는 경우를 제외.(none과 none일 경우 1가지)
    return answer - 1

print(solution([['yellowhat', 'headgear'], ['bluesunglasses', 'eyewear'], ['green_turban', 'headgear']]))

# Counter를 사용
from collections import Counter
# reduce는 누적을 해야될 때 여러번 해야하는 동작을 줄여준다.
from functools import reduce

def solution(clothes):
    # clothes에서 cloth, type이 있는데 type을 counter에 사용하겠다.
    counter = Counter([type for cloth, type in clothes])
    print(counter.values())

    # reduce는 어떤 함수를 여러번 적용하기 때문에 함수를 정의해야한다(lambda).
    # reduce함수에서 lambda acc, cur: acc * (cur + 1)동작을 반복해서 누적한다.
    # cur값은 counter.values()를 전달하고 초기값은 1로 지정해준다.
    answer = reduce(lambda acc, cur: acc * (cur + 1), counter.values(), 1)
    return(answer) - 1


print(solution([['yellowhat', 'headgear'], ['bluesunglasses', 'eyewear'], ['green_turban', 'headgear']]))