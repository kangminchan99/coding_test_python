def solution(n_str):
#   시작부분이 0 이면 0을 지우게 n_str에 바꿔준다.  
    while n_str.startswith('0'):
        n_str = n_str[1:]
            
    return n_str