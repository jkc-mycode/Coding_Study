def solution(bandage, health, attacks):
    total_time = attacks[-1][0]
    max_health = health
    success = 0
    
    for t in range(1, total_time + 1):
        is_attacked = False
        for attack in attacks:
            if attack[0] == t:
                health -= attack[1]
                success = 0
                is_attacked = True
        
        if not is_attacked:
            success += 1
            if success == bandage[0]:
                health = health + bandage[1] + bandage[2]
                success = 0
            else:
                health = health + bandage[1]
                
            if health > max_health:
                health = max_health
        
        if health <= 0:
            return -1

    return health