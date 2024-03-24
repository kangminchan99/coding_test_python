def solution(num_list):
    odd = []
    even = []
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
        
    
#   정수형 리스트를 하나로 이어서 붙이기
    oddSum = ''.join(map(str, odd))
    evenSum = ''.join(map(str, even))
    
    return int(oddSum) + int(evenSum)
    