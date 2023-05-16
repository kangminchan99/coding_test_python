def solution(record):
    answer = []
    userId = {}

    
    for str in record:
        strlist = str.split()
        entrance = strlist[0]
        if entrance == 'Enter' or entrance  == 'Change':
            uid = strlist[1]
            name = strlist[2]
            userId[uid] = name
    
    for str in record:
        strlist = str.split()
        entrance = strlist[0]
        if entrance == 'Enter':
            id = strlist[1]
            answer.append(userId[id] + '님이 들어왔습니다.')
        elif entrance == 'Leave':
            id = strlist[1]
            answer.append(userId[id] + '님이 나갔습니다.')
            
    return answer
            
            
            