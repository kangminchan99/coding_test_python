def solution(my_string, indices):
    answer = []
    for i in range(len(indices) -1 , 0 , -1):
        for j in range(i):
            save = 0
            if indices[j] > indices[j + 1]:
                save = indices[j + 1]
                indices[j + 1] = indices[j]
                indices[j] = save
    
    for i in range(len(my_string)):
        if i not in indices:
            answer.append(my_string[i])
        
    return ''.join(answer)
            