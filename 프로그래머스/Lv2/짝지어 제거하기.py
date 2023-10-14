def solution(s):
    stack = []
    
    # s만큼 반복
    for char in s:
        # 두개의 스택의 char이 같을경우 둘다 제거
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # 아닐경우 append
            stack.append(char)
    
    # 길이가 0이면 1 아니면 0
    if len(stack) == 0:
        return 1
    else:
        return 0
    