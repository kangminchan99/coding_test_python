# 주로 sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬할 수 있도록 하는 모듈
from operator import itemgetter

def solution(food_times, k):
    foods = []
    foodType = len(food_times)
    
    for f in range(foodType):
        # 음식의 순서와 번호를 지정해준다.
        foods.append((food_times[f], f + 1))
    
    # foods[0] - 음식을 먹는데 걸리는 시간
    # foods[1] - foods의 인덱스 위치
    foods.sort()
    
    pretime = 0
    # enumerate - 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
    for i, food in enumerate(foods):
        print(i, food)
        # diff = 높이
        diff = food[0] - pretime
        if diff != 0:
            # spend = 소비한 시간
            spend = diff * foodType
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= foodType
                sublist = sorted(foods[i:], key = itemgetter(1))
                return sublist[k][1]
                
        foodType -= 1
        
    # 만약 더 섭취해야 할 음식이 없다면 -1을 반환
    return -1