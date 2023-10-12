def solution(s):
    # 공백을 기준으로 구분
    a = s.split()
    # 반복문을 돌며 capitalize()를 적용하여 문자의 첫글자가 소문자일 경우 대문자로 변경
    b = [word.capitalize() for word in a]
    # 공백을 포함하여 합쳐주기
    result = ' '.join(b)
    print(result)