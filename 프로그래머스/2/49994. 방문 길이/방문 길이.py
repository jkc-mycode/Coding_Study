def solution(dirs):
    result = 0
    dist = set()
    cur_location = [0, 0]
    
    for d in dirs:        
        prev_location = list(cur_location)
        if d == "U":
            cur_location[1] += 1
        elif d == "D":
            cur_location[1] -= 1
        elif d == "R":
            cur_location[0] += 1
        elif d == "L":
            cur_location[0] -= 1
        
        if abs(cur_location[0]) > 5 or abs(cur_location[1]) > 5:
            cur_location = list(prev_location)
            continue

        dist.add(frozenset([tuple(prev_location), tuple(cur_location)]))
        
    return len(dist)
    