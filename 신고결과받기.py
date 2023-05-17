def solution(id_list, report, k):
    reportHash = {}
    resultHash = {}
    
    for r in report:
        # 신고유저, 불량유저
        user, bad = r.split()
        if user not in reportHash:
            # set()- 중복값 허용 X.
            reportHash[user] = set()
        reportHash[user].add(bad)
        print(reportHash[user])
            
        if bad not in resultHash:
            resultHash[bad] = set()
        resultHash[bad].add(user)
        
    answer = [0 for _ in range(len(id_list))]
    for i in range(len(id_list)):
        user = id_list[i]
        if user not in reportHash:
            continue
        for bad in reportHash[user]:
            if len(resultHash[bad]) >= k:
                answer[i] += 1
    return answer