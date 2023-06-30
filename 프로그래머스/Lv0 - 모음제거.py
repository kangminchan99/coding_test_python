def solution(my_string):
    dic = {'a', 'e', 'i', 'o', 'u'}
    result = ''
    for i in my_string:
        if i not in dic:
            result += i
            
    return result