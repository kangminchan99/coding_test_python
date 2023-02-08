# # 1. Loop활용

# def solution(phone_book):
#     # 비교할 A선택
#     for i in range(len(phone_book)):
#     # 비교할 B선택
#         for j in range(i + 1, len(phone_book)):
#     # 서로가 서로의 접두어인지 확인
#             if phone_book[i].startswith(phone_book[j]):
#                 return False
#             if phone_book[j].startswith(phone_book[i]):
#                 return False

#     return True

# print(solution(["6", "12", "6789"]))

# # 2. Sorting/Loop 활용

# def solution(phone_book):
#     # 전화번호 sort
#     phone_book.sort()
#     # sort 한 전화번호를 2개씩 확인해서 접두어인지 본다.
#     for i in range(len(phone_book) -1):
#         if phone_book[i+1].startswith(phone_book[i]):
#             return False
#     return True

# print(solution(["6", "12", "789"]))

# # 3. Zip사용(두개에서 하나 씩 뽑아 와야 할 때 사용)
# def solution(phone_book):
#     # 전화번호 sort
#     phone_book.sort()

#     print(list(zip(phone_book, phone_book[1:])))
#     # 자료형을 묶어 하나의 튜플로 만들어준다.
#     for p1, p2 in zip(phone_book, phone_book[1:]):
#         if p2.startswith(p1):
#             return False

#     return True


# print(solution(["6", "12", "789"]))

# 4. hash활용
def solution(phone_book):
    # 해시 맵을 만들고, value값을 1로 설정 
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1
    # 접두어가 해시맵에 존재하는지 찾는다.
    for phone_number in phone_book:
        jubdoo = ''
        for number in phone_number:
            jubdoo += number
            # 접두어를 찾는다.(기존 번호와 같은 경우는 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False

    return True


print(solution(["6", "12", "6789"]))




