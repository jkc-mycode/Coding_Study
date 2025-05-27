from itertools import permutations

def solution(k, dungeons):
    result = []
    temp_k = k
    per_dungeons = permutations(dungeons)
    
    for dungeon in per_dungeons:
        temp_k = k
        count = 0
        for value in dungeon:
            if temp_k >= value[0]:
                count += 1
                temp_k -= value[1]
            else:
                break
        result.append(count)
    
    return max(result)