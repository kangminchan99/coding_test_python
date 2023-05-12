def solution(cacheSize, cities):
    # LRU - 가장 오랫동안 사용되지 않은것부터 사용
    Cache = []
    # 실행시간
    Time = 0
    for city in cities:
        # 공백, 숫자, 특수문자 등이 없는 영문자로, 대소문자 구분을 하지 않으므로 소문자로 바꿔준다.
        city = city.lower()
        # hit
        if city in Cache:
            Cache.remove(city)
            Cache.append(city)
            Time += 1

        # miss
        else:
            Cache.append(city)
            if cacheSize < len(Cache):
                Cache.pop(0)
            Time += 5
    return Time