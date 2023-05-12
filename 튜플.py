def solution(s):
    # 문자열로 되어있는 s를 하나의 튜플로 빼줌
    # eval("") - 문자열로 되어있는 것을 그자체로 바꿔주는것
    # Ex) eval("5+7")의 실행결과는 7로 나온다.
    # "{{2},{2,1},{2,1,3},{2,1,3,4}}"를 eval해도 에러가 발생한다 그이유는 {{}}형식으로 되어있기 때문에 짤라줘야한다.
    nums = eval(s[1:-1])
    if len(nums) > 1 :
        # 오름차순으로 정렬
        nums = sorted(nums, key=lambda n: sum(n))
    else:
        return list(nums)
    
    result = []
    for num in nums:
        for n in num:
            if n not in result :
                result.append(n)
    return result




