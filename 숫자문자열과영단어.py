
# 딕셔너리는 함수 밖에서 선언하자 ^^
dict = { '1' : 'one', '2' :  'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine'}

def solution(s):
    answer = s


    # value값을 키로 바꿔주기 딕셔너리가 둘다 문자열이면 replace에 두개를 넣어줄 수 있다.
    for key, value in dict.items():
        answer = answer.replace(value, key)
    return int(answer)