def solution(cards1, cards2, goal):
    cntCard1 = 0
    cntCard2 = 0
    for i in range(len(goal)):
        if cntCard1 < len(cards1) and goal[i] == cards1[cntCard1] :
            cntCard1 += 1
        elif cntCard2 < len(cards2) and goal[i] == cards2[cntCard2] :
            cntCard2 += 1
        else:
            return "No"
        
    return "Yes"