def solution(nums):
    get = len(nums) // 2
    dic = {}

    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
            
    if len(dic) > get:
        return get
    else:
        return len(dic)