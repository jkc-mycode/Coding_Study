from collections import Counter

def solution(k, tangerine):
    result = 0
    tang = sorted(Counter(tangerine).values(), reverse=True)
    
    for value in tang:
        if k <= 0:
            break
        k -= value
        result += 1
    
    return result
            