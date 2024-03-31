def solution(myString):
    a = myString.split('x')
    
#   a 리스트안에 ""이 없는것들만 다시 저장
#   list(filter(lambda x:x != "", a))
    conv_a = list(filter(lambda x: x!= "", a))

    
#   sorted를 사용하면 정렬된 새로운 리스트를 반환, 원본 리스트 변경 X, sort는 원본 리스트 변경
    return sorted(conv_a)