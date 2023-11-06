def solution(n):
    answer = 0
    target_one_count = get_one_count_from_binary_number(n)
    current_n = n
    while True:
        current_n += 1
        current_one_count = get_one_count_from_binary_number(current_n)
        if current_one_count == target_one_count:
            return current_n
    return answer

def get_one_count_from_binary_number(num: int) -> int:
    return_value: int = 0
    while True:
        num, remainder = divmod(num, 2)
        return_value += remainder
        if num == 0:
            return return_value