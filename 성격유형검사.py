def solution(survey, choices):
    answer = ''
    dict = {'R':0, 'T':0, 'C':0, 'F': 0, 'J':0,'M':0, 'A':0, 'N':0}
    # 1	매우 비동의 3점
    # 2	비동의 2점
    # 3	약간 비동의 1점
    # 4	모르겠음 0점
    # 5	약간 동의 1점
    # 6	동의 2점
    # 7	매우 동의 3점
    # 점수 변경해주기
    mapping = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}

    
    for i in range(0, len(choices)):
        choice = choices[i]
        
        # CF - 콘 프로도형 4보다 작으면 콘형이므로 survey[i][0]
        if choice < 4:
            key = survey[i][0]
            dict[key] += mapping[choice]
        elif choice > 4:
            key = survey[i][1]
            dict[key] += mapping[choice]
    

    
    jipyo = [['R', 'T'], ['C','F'], ['J', 'M'], ['A', 'N']]
    
    for j in jipyo:
        c1 = j[0]
        c2 = j[1]
        
        if dict[c1] == dict[c2]:
            if c1 < c2:
                answer += c1
            else:
                answer += c2
        elif dict[c1] > dict[c2]:
            answer += c1
        else:
            answer += c2
            
    return answer
                