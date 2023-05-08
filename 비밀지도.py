# 이진수로 나타내기
a = bin(9)
b = bin(30)
# 01001
# 11110
# ------ or 연산
# 11111을 출력해야됨
print(a)
print(b)

# # 앞에 0b제거
# bin(9)[2:] bin(30)[2:]

# 9와 30을 한번에 2진연산(or연산으로)해주고 1을 #로, 0은 공백으로 replace
c  = bin(9|31)[2:].replace('1', '#').replace('0', ' ')
print(c)

# 문자열에서 자리수 맞춰주는 메서드
# ex)
# s = 'Hello'
# width = 10
# s.rjust(width) - s를 넓이 10에서 오른쪽 정렬
# right_aligned = s.rjust(width)
# s.ljust(width) - s를 넓이 10에서 왼쪽 정렬
# left_aligned = s.ljust(width)

# 문제
arr1 = [9, 20, 28, 18,11]
arr2 = [30, 1, 21, 17, 28]
# 5자리 수로 표현 ex) 5 = 00101
n = 5

# for i로 두면(9, 30)처럼 패킹돼서 출력되는데, for i,j로두면 언패킹이되어 9 30 형태로 출력된다.
# zfill - 문자열의 왼쪽에 0을 추가하여 문자열의 길이를 지정된 길이로 맞추는 파이썬의 내장 메서드
for i, j in zip(arr1,arr2):
    print(bin(i|j)[2:].zfill(n).replace('1', '#').replace('0', ' '))

# 코딩테스트 연습
def solution():
    
    answer = []
    for i, j in zip(arr1,arr2):
        #  answer.append - 리스트의 맨 뒤에 새로운 요소를 추가하는 메서드입니다.
        answer.append(bin(i|j)[2:].zfill(n).replace('1', '#').replace('0', ' '))
        return answer


