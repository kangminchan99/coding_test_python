def solution(code):
    answer = []
    dic = {'mode': 0}
    
    for i in range(len(code)):
        if code[i] == '1' and dic['mode'] == 0:
            dic['mode'] = 1
            continue
        
        if code[i] == '1' and dic['mode'] == 1:
            dic['mode'] = 0 
            continue
            
            
        if code[i] != '1' and dic['mode'] == 0 and i % 2 == 0:
            answer.append(code[i])
            
        if code[i] != '1' and dic['mode'] == 1 and i % 2 != 0:
            answer.append(code[i])
            
        

# ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.    
    if answer == []:
        answer.append("EMPTY")

    
    return ''.join(answer)
        
            