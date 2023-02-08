def solution(participant, completion):
    # 1. sorting(리스트 정렬)한다.
    participant.sort()
    completion.sort()

    # 2. completion list의 length만큼 돌면서 particioant에만 존재하는 한 명 찾기 
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    # 3. 리스트를 찾아도 답이없으면 participant의 마지막 주자가 완주하지 못한 선수이다.
    return participant[-1]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))


# def solution(participant, completion):
#     hashDict = {}
#     sumHash = 0
#     # 1. particioant의 리스트의 hash를 구하고, 합을 구한
#     # ex) leo = key(5), kiki = key(7) eden = key(13)의 합
#     for p in participant:
#         hashDict[hash(p)] = p
#         sumHash += hash(p)


#     # 2. completion list의 hash를 빼준다.
#     # ex) kiki = key(7) eden = key(13)의 차이를 구한다.  
#     for c in completion:
#         sumHash -= hash(c)

#     # 3. 남은 값이 완주하지 못한 선수의 hash값이 된다.
#     return hashDict[sumHash]


# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

# from collections import Counter
# def solution(participant, completion):
#     # 1. participant의 counter를 구한다.
#     p_counter = Counter(participant)

#     # 2. completion의 카운터를 구한다.
#     c_counter = Counter(completion)

#     # 3. 둘의 차를 구하고 key를 구한다.
#     answer = p_counter - c_counter
#     print(p_counter)
#     return list(answer)
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))


