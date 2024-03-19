def solution(num_list):
        
#    버블 정렬

#   바깥 반복문에서 리스트의 길이만큼 ex) 6이면 5부터 0까지 역순으로 반복을 돈다. 버블 정렬 수행 처음 시 가장 큰 수가 마지막에 들어간다
    for i in range(len(num_list) - 1, 0, -1):
#       2. 내부 반복문에서 리스트의 앞 뒤를 서로 비교해가며 정렬 반복
        for j in range(i):
            change = 0
            if num_list[j] > num_list[j + 1]:
#               서로의 값을 바꿔준다.
                change = num_list[j + 1]
                num_list[j + 1] = num_list[j]
                num_list[j] = change
    return num_list[:5]
                