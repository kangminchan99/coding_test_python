def solution(arr, query):
#   index 0,1,2 value 4,1,2 
#   enumerate -> index value값 뽑기
    for index, value in enumerate(query):
        if index % 2 == 0:
            arr = arr[:value+1]
        else:
            arr = arr[value:]
    
    return arr
        
                