def solution(n, words):
    # 중복을 방지
    words_set = set()
    words_set.add(words[0])
    for i in range(1, len(words)):
        # 셋 안에 있거나 words 뒤의 것의 마지막 알파벳과 앞의 알파벳의 첫번째가 다르면 
        if (words[i] in words_set) or (words[i-1][-1] != words[i][0]):
            # 번호는 i를 사람수로 나눈 것 + 1 why? 반복문에서 처음 시작하는 1은 두번째 사람이므로
            # 차례는 i를 사람 수로 나눈 몫에 1을 더한값
            return([(i%n) + 1, (i//n +1)])
        
        words_set.add(words[i])
        
    return [0,0]