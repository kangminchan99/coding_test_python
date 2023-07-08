def solution(my_string, overwrite_string, s):
    a = ''
    a += my_string[0:s]
    a += overwrite_string
    a += my_string[s+len(overwrite_string):]
    return a
        