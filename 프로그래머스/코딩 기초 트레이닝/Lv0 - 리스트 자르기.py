def solution(n, slicer, num_list):
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]
    
    dic = {1: num_list[0:b+1],
           2: num_list[a:],
           3:num_list[a:b+1],
           4:num_list[a:b+1:c]}
    
    if n in dic:
        return(dic[n])
