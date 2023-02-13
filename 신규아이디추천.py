def solution(new_id):
    answer = ''
    # 소문자로 치환
    new_id = new_id.lower()
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    # isalnum() - 알파벳과 숫자로만 구성되었는지 확인
    for a in new_id:
        if a.isalnum() or a in '-_.':
            answer += a

    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 마침표(.)가 처음이나 끝에 위치한다면 제거
    # answer가 존재하는데 answer 0부터 1까지가 '.'이라면 answer의 1뒤에 있는 것을 가져오겠다.
    # answer가 존재하는데 answer -1부터 0까지가 '.'이라면 answer의 -1뒤에 있는 것을 가져오겠다.
    if answer and answer[0 ]== '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    # 빈 문자열이라면, new_id에 "a"를 대입
    if answer == '':
        answer = 'a'
    # 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거. 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다
    while len(answer) < 3:
        answer += answer[-1]
    return answer

print((solution("abcdefghijklmn.p")))