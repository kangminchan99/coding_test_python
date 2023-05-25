from bisect import bisect_left

def solution(info, query):
    # 모든 경우의 수를 매핑
    infomap = {'-':0, 'cpp':1, 'java':2, 'python':3, 
              'backend':1, 'frontend':2,
              'junior':1, 'senior':2, 
              'chicken':1, 'pizza':2}
    
    # 1차원 배열로 []로 채우기 
    slist = [[] for _ in range(4*3*3*3)]
    
    # info로 받은 정보 저장
    for i in info:
        inf = i.split()
        # slist의 인덱스를 만들기 위해 arr라는 튜플 생성
        arr = (infomap[inf[0]] *3 *3 *3,
               infomap[inf[1]] *3 *3,
               infomap[inf[2]] *3 ,
               infomap[inf[3]])
        score = int(inf[4])
        
        # 비트형태로 부분집합 나타내기
        # 원소가 언어,직군,경력, 소울푸드 4가지니까 1왼쪽으로 4만큼 시프트
        for x in range(1<<4):
            idx = 0
            for y in range(4):
                if x & (1 << y):
                    idx += arr[y]
            slist[idx].append(score)
            
    for i in range(4*3*3*3):
        slist[i] = sorted(slist[i])
            
    answer = []
    for string in query:
        w = string.split()
        idx = infomap[w[0]] *3 *3 *3 + infomap[w[2]]*3*3+ infomap[w[4]]*3 + infomap[w[6]]
        score = int(w[7]) # 100 200 300
        # bisect_left - 첫번째 정렬된 리스트를 score라는 새로운 값을 넣었을 때 
        # 여전히 정렬된 값을 넣기위해 어디에 넣어야 되는지 알려준다.
        answer.append(len(slist[idx]) - bisect_left(slist[idx], score)) # 50일 경우 0을 반환해줌, 150이면 1
        
        
        
    return answer