def solution(my_string, is_suffix):
    leng = len(is_suffix)
    a = my_string[-leng:]
    if (a == is_suffix):
        return 1
    else:
        return 0