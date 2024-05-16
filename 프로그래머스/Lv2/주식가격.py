def solution(prices):
    answer = []
    lenAll = len(prices[::])
    lenP = len(prices)
    for i in range(lenP):
        check = prices[i]
        cnt = 0
        for j in range(i + 1, lenAll):
            if check <= prices[j]:
                cnt += 1
            else:
                cnt = j - i
                break
            
        answer.append(cnt)
    return answer
        