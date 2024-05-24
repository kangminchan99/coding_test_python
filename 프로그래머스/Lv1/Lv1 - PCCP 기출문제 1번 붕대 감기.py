def solution(bandage, health, attacks):
#   bandage[5, 1, 5] =  [시전 시간, 초당 회복량, 추가 회복량] 
    maxHp = health
    turn = 0
    for i in range(1, attacks[-1][0] + 1):
        if i == attacks[0][0]:
            health -= attacks[0][1]
            del attacks[0]
            
            if health <= 0:
                return -1 
            else:
                turn = 0
                continue
        
        if health <= maxHp:
            health += bandage[1]
            if health > maxHp:
                health = maxHp
            turn += 1
        
        if turn == bandage[0]:
            health += bandage[2]
            if health >= maxHp:
                health = maxHp
            turn = 0
            
            
    return health