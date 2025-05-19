def solution(brown, yellow):
    total = brown + yellow
    result = []
    for i in range(3, total//2):
        if total % i == 0:
            result.append(total // i)
    
    for y in result:
        x = total // y
        if x >= y and (x-2) * (y-2) == yellow:
            return [x, y]
    
        
            
        