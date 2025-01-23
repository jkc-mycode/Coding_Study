def solution(dirs):
    directions = {
        "U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)
    }
    result = 0
    dx = 0
    dy = 0
    visited_way = []
    
    for i in dirs:
        x, y = directions[i]
        nx, ny = dx + x, dy + y
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            next_way = {(dx, dy), (nx, ny)}
            if next_way not in visited_way:
                visited_way.append(next_way)
                result += 1
            dx, dy = dx + x, dy + y

    return result