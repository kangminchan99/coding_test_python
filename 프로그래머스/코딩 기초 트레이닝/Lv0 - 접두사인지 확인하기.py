def solution(my_string, is_prefix):
    prelen = len(is_prefix)
    if my_string[:prelen] == is_prefix:
        return 1
    else:
        return 0