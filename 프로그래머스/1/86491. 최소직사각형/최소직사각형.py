def solution(sizes):
    for val in sizes:
        val.sort()
    
    maxW = -1
    maxH = -1
    for val in sizes:
        if val[0] > maxW:
            maxW = val[0]
        if val[1] > maxH:
            maxH = val[1]
            
    return maxW * maxH