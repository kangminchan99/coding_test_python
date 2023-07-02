def solution(arr):
    count = -1

    while True:
        # 안에서 answer선언해주고
        answer = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                answer.append(i // 2)
            elif i < 50 and i % 2 != 0:
                answer.append(i * 2 + 1)
            else:
                answer.append(i)
        
        count += 1
        if arr == answer:
            return count
        
        # arr을 answer로 바꿔준다
        arr = answer