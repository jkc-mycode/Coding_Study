from collections import Counter

def solution(k, tangerine):
    result = 0
    tang_dict = dict(sorted(Counter(tangerine).items(), key=lambda x: x[1], reverse=True))
    
    for key, value in tang_dict.items():
        if k <= 0:
            break
        k -= value
        result += 1
    
    return result
            