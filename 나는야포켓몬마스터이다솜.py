# 0. 입력 및 초기화
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 1. N개의 정보를 hash에 반영
idx_to_name = {}
name_to_idx = {}
for i in range(1, N+1):
    name = input().rstrip()
    idx_to_name[i] = name
    name_to_idx[name] = i

# 2. M개의 쿼리를 해시를 통해 출력
for _ in range(M):
    query = input().rstrip()
    # isdigit() - 문자가 '단 하나'라도 있다면 False를 반환하고, 
    # 모든 문자가 '숫자'로만 이루어져있으면 True를 반환합니다.
    if query.isdigit():
        print(idx_to_name[query])
    else:
        print(name_to_idx[query])