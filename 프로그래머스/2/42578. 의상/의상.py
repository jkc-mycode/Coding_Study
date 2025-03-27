def solution(clothes):
    clothes_dict = {}
    for c in clothes:
        if not clothes_dict.get(c[1]):
            clothes_dict[c[1]] = []
        clothes_dict[c[1]].append(c[0])
    
    result = 1
    for v in clothes_dict.values():
        result *= (len(v) + 1)
    
    return result - 1