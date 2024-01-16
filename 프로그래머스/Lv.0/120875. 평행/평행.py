from itertools import combinations

def get_sub(a, b):
    return abs(a[1] - b[1]) / abs(a[0] - b[0])
    

def solution(dots):
    for a, b in list(combinations(combinations(dots, 2), 2)):
        if len(set(tuple(i) for i in a).union(set(tuple(i) for i in b))) == 4:
            if get_sub(*a) == get_sub(*b):
                return 1
    return 0
            
        
        