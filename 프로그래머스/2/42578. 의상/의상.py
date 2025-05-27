def solution(clothes):
    result = 1
    clth_dict = {}
    for c in clothes:
        if clth_dict.get(c[1]) == None:
            clth_dict[c[1]] = []
        clth_dict[c[1]].append(c[0])
    
    for _,value in clth_dict.items():
        result *= len(value) + 1
    
    return result - 1