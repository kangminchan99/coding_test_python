# 이진변환
def binary_transform(s):
    # s길이 - 0제거한 길이 = 제거한 0의 개수
    a = len(s) - len(s.replace("0", ""))
    s = s.replace("0", "")
    
    return bin(len(s))[2:], a

def solution(s):
    count = 0
    remove_zero = 0
    while s != "1":
        s, zeros = binary_transform(s)
        count += 1
        remove_zero += zeros
        
    return [count, remove_zero]
        

            
            