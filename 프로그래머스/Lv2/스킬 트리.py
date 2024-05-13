def solution(skill, skill_trees):
    # 스킬트리 맞는거 체크
    answer = 0
    # 스킬트리 순환
    for i in skill_trees:
        # 기본값 true
        possible = True
        # 스킬 순서 인덱스
        skill_idx = 0
        # 스킬트리[index] 순환
        for j in i:
            # skill에 포함되어 있는 경우
            if j in skill:
                # 스킬의 0번째와 스킬 순서가 일치하는지 체크
                curr_skill_idx = skill.index(j)
                # 다를경우 false후 break
                if curr_skill_idx != skill_idx:
                    possible = False
                    break
                # 스킬 인덱스를 1증가하여 다음과 비교
                skill_idx += 1
        # 이상없을 경우 answer += 1
        if possible:
            answer += 1
            
    return answer
                