from collections import Counter

def solution(weights):
    result = 0
    weights = Counter(weights)
    
    for w in weights:
        result += weights[w] * (weights[w] -1 ) // 2
        result += weights[w] * weights[w * 4 / 2]
        result += weights[w] * weights[w * 4 / 3]
        result += weights[w] * weights[w * 3 / 2]
    
    return result