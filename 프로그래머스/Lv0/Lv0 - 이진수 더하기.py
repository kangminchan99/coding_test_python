def solution(bin1, bin2):
    intBin1 = bin1
    intBin2 = bin2
    
    # 10진수로 변환
    decimal = int(intBin1 , 2) + int(intBin2, 2)
    
    # 2진수로 변환
    changeBin = bin(decimal)
    
    # '0b' 0과 1만 나오게 출력
    result = changeBin[2:]
    
    return result
    
    