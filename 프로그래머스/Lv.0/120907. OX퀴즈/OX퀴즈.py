def solution(quiz):
    result = []
    
    for i in quiz:
        p = i.split(" ")
        z = int(p[0])
        print(p)
        for i in range(2, len(p)-2, 2):
            if p[i-1] == '+':
                z += int(p[i])
            elif p[i-1] == '-':
                z -= int(p[i])
            
        if z == int(p[-1]):
            result.append('O')
        else:
            result.append('X')
            
    return result
            
            
        