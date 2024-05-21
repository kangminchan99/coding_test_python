def solution(my_string):
    result = ''
    for i in my_string:
        if i.isupper() == True:
            result += i.lower()
        else:
            result += i.upper()
    return result
        