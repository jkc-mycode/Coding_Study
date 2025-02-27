def solution(brown, yellow):
    total = brown + yellow
    
    for y in range(3, int(total**0.5)+2):
        if total % y == 0:
            x = total // y
            if x >= y and (x-2) * (y-2) == yellow:
                return [x, y]