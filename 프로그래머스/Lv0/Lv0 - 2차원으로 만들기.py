def solution(num_list, n):
    answer = []
    lenN = len(num_list)
    for i in range(0, lenN, n):
        answer.append(num_list[i:i+n])
    return answer