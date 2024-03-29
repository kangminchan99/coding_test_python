def solution(myStr):
    one = myStr.replace('b', 'a')
    # print(one)
    two = one.replace('c', 'a') 
    # print(two)
    
    listTwo = two.split('a')
    
    # listTwo안에서 ''(None)이 없는 것들만 리스트에 다시 저장한다.
    answer = list(filter(None, listTwo))
    
    if len(answer) != 0:
        return answer
    else:
        return ["EMPTY"]