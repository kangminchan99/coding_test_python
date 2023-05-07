# 1부터 10000까지 8은 총 몇번 나오는가? ex) 8088 = 3, 8888 = 4로 계산

# 1. 범위를 리스트로 묶어 문자열로 변환시켜 count를 사용하여 계산.
a = str(list(range(1,10001))).count('8')
print(a)

# 2. 반복문으로 계산
count = 0
for i in range(10001):
    if '8' in str(i):
        count += str(i).count('8')

print(count)