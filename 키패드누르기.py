def getnearHand(l, r, keyDict,n, hand):
    # abs - 절댓값
    left_distance = abs(keyDict[l][0] - keyDict[n][0]) + abs(keyDict[l][1] - keyDict[n][1])
    right_distance = abs(keyDict[r][0] - keyDict[n][0]) + abs(keyDict[r][1] - keyDict[n][1])

    
    if left_distance == right_distance:
        nearHand = 'L' if hand == 'left' else 'R'
    # 3항 연산자 - python
    else:
        nearHand = 'L' if left_distance < right_distance else 'R'
    
    return nearHand
    

def solution(numbers, hand):
    leftKey = [1,4,7]
    rightKey = [3,6,9]
    handPosition = ['*', '#']
    
    keyDict = {
        1: (0,0), 2:(0,1), 3: (0,2),
        4: (1,0), 5:(1,1), 6: (1,2),
        7: (2,0), 8:(2,1), 9: (2,2),
        '*': (3,0), 0:(3,1), '#': (3,2),
    }
    
    result = ''
    for n in numbers:
        # n 이 leftKey에 있으면 왼손이 누른다.
        if n in leftKey:
            result += 'L'
            handPosition[0] = n
        # n 이 rightKey에 있으면 오른손이 누른다.
        elif n in rightKey:
            result += 'R'
            handPosition[1] = n
        else:
            # 더 가까운 손으로 누른다.
            nearHand = getnearHand(handPosition[0], handPosition[1], keyDict,n, hand)
            if nearHand == 'L':
                result += 'L'
                handPosition[0] = n
            else:
                result += 'R'
                handPosition[1] = n
                
    return result
            