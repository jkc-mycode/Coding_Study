def solution(dirs):
    result = set()
    dist = {
        "U": [0, 1],
        "D": [0, -1],
        "R": [1, 0],
        "L": [-1, 0],
    }
    x, y = 0, 0
    
    for d in dirs:
        dx = x + dist[d][0]
        dy = y + dist[d][1]
        
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            result.add((x, y, dx, dy))
            result.add((dx, dy, x, y))
            x, y = dx, dy
    
    return len(result)//2
