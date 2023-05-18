def solution(n, info):
    # 0~ 10까지 총 11개를 반환,값은 0으로
    answer = [0 for _ in range(11)]
    # 라이언의 화살정보 리스트 생성
    tmp = [0 for _ in range(11)]
    # 초기값을 0으로 해서 차이값이 큰값이 나올때마다 변경
    maxDiff = 0
    
    # range() 함수를 사용하여 0부터 2^10 - 1까지의 범위 지정
    for subset in range(1, 1 << 10):
        ryan = 0
        apeach = 0
        # 화살개수 - 지정한 화살보다 많이 또는 적게 쐈는지 카운팅하기위해
        cnt = 0
        
        for i in range(10):
            if subset & (1 << i):
                ryan += 10 - i
                tmp[i] = info[i] + 1
                cnt += tmp[i]
            else:
                tmp[i] = 0
                if info[i]:
                    apeach += 10 - i
        if cnt > n: continue
        
        tmp[10] = n - cnt
        
        if ryan - apeach == maxDiff:
            for i in reversed(range(11)):
                if tmp[i] > answer[i]:
                    maxDiff = ryan - apeach 
                    answer = tmp[:]
                    break
                elif tmp[i] < answer[i]:
                    break
        elif ryan - apeach > maxDiff:
            maxDiff = ryan - apeach 
            answer = tmp[:]
    
    if maxDiff == 0:
        answer = [-1]
        
    return answer