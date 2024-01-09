def solution(dots):
    x = []
    y = []
    for i in dots:
        x.append(i[0])
        y.append(i[1])
        
    width = max(x) - min(x)
    height = max(y) - min(y)
    
    return width * height