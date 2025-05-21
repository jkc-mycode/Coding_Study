from collections import defaultdict

def solution(k, tangerine):
    result = 0
    dict_tang = defaultdict(int)
    for i in tangerine:
        dict_tang[i] += 1
    
    dict_tang = dict(sorted(dict_tang.items(), key=lambda x: x[1], reverse=True))
    
    for key, value in dict_tang.items():
        if k <= 0:
            return result
        k -= value
        result += 1
    
    return result