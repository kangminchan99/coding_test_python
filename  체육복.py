# # Set을 활용
# def solution(n, lost, reserve):
#     # 1. Set을 만든다
#     # reserve_only - reserve 와 lost에 존재하는 학생을 뺀 정말로 체육복을 빌려줄 수 있는 학생들
#     reserve_only = set(reserve) - set(lost)
#     # lost_only - reserve와 lost에 둘다 존재하는 학생들을 lost에서 빼주고 순수하게 체육복이 필요한 학생들
#     lost_only = set(lost) - set(reserve)
#     # 2. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
#     # reserve_only에서 reserve를 하나씩 빼온다.
#     for reserve in reserve_only:
#         front = reserve - 1
#         back = reserve + 1
#         # 만약 lost_only(체육복이 필요한 학생)가 앞에 있다면 체육복을 줬으므로 lost_only에서 빼준다.
#         if front in lost_only:
#             lost_only.remove(front)
#         # 만약 lost_only(체육복이 필요한 학생)가 뒤에 있다면 체육복을 줬으므로 lost_only에서 빼준다.    
#         elif back in lost_only:
#             lost_only.remove(back)
#     # 3. 전체 학생 수에서 lost 학생 수를 빼준다. 
#     return n - len(lost_only)

# print(solution(5,[2,4],[1,3,5]))


# 배열 활용
def solution(n, lost, reserve):
    # 1. 학생 배열 생성 - 0으로 존재하는 n+2만큼의 배열,
    # 전체 학생 수(n)의 맨처음과 맨뒤에 허수를 추가(n+2)하여 앞 뒤를 확인하는 코드를 만들어 줄 수 있다.
    student = [0] * (n+2)
    # 2. reserve 와 lost 정보 반영
    for r in reserve:
        student[r] += 1
    for l in lost:
        student[l] -= 1
    # 3. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for i in range(1, n+1):
        if student[i] > 0:
            front = i + 1
            back = i - 1
            if student[front] < 0:
                student[i] -= 1
                student[front] += 1
            elif student[back] < 0:
                student[i] -= 1
                student[back] += 1
    # 4. 체육복을 가지고 있는 학생 수를 계산
    answer = 0
    for i in range(1, n+1):
        if student[i] >= 0:
            answer += 1
    return answer
print(solution(5,[2,4],[1,3,5]))