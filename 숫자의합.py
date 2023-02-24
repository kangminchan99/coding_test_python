# # 범용적 풀이
# # 0. 입력 및 초기화
# N = int(input())
# arr = input()
# print(arr)
# # 1. arr을 정수로 변환하여 누적
# answer = 0
# for i in range(len(arr)):
#     answer += int(arr[i])5
# # 2. 출력
# print(answer)

# pythonic 풀이
input
print(sum(map(int, input())))
