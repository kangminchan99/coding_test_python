def solution(lottos, win_nums):
    dic = {'6': 1, '5':2 , '4':3 , '3': 4, '2':5, '1':6, '0': 6}
    answer = [0,0]
    cnt = 0
    fcnt = 0
    for i in lottos:
        if i == 0:
            fcnt += 1
        if i in win_nums:
            cnt += 1

    answer[0] = dic[str(fcnt + cnt)]
    answer[1] = dic[str(cnt)]
    
    return answer

    