def convert(time):
    h, m , s = time.split(':')
    # 스플릿 후 시간, 분을 초로 변환하여 리턴
    return int(h) * 60 * 60 + int(m) * 60 + int(s)

def solution(play_time, adv_time, logs):
    playSec = convert(play_time)
    advSec = convert(adv_time)
    
    totalSec = [0 for _ in range(playSec + 1)]

    for log in logs:
        startLog, endLog = log.split('-')
        start = convert(startLog)
        end = convert(endLog)
        # 시작 로그 부분을 전부다 1로 마킹, 끝 로그 부분은 사람이 빠지는 부분이므로 -1로 마킹
        totalSec[start] += 1
        totalSec[end] -= 1
        
    for i in range(1, playSec):
        # 앞 인덱스랑 더해준다
        totalSec[i] += totalSec[i-1]
    
    # 처음부터 광고 길이까지 누적 합 구하기
    currSum = sum(totalSec[:advSec])
    
    maxSum = currSum
    maxIdx = 0
    for i in range(advSec, playSec):
        currSum = currSum + totalSec[i] - totalSec[i - advSec]
        if currSum > maxSum:
            maxSum = currSum
            maxIdx = i - advSec + 1
            
    
    # 시,분,초 형태로 다시 반환
    answer = '%02d:%02d:%02d' % (maxIdx/3600, maxIdx/60 % 60, maxIdx %60)
    return answer