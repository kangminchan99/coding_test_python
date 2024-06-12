def prime_factors(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n /= i
        else:
            i += 1
    
    return answer
    

def solution(n):
    result = prime_factors(n)
    answer = []
    for i in set(result):
        answer.append(i)
    
    return sorted(answer)
        