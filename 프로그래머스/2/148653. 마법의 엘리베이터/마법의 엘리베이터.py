def solution(storey):
    result = 0
    c = len(str(storey)) - 1
    
    while storey > 0:
        if storey <= 5:
            result += storey
            break
        div = storey // pow(10, c)
        if div > 5 or div == 5 and int(str(storey)[1]) >= 5:
            storey = pow(10, c+1) - storey
            result += 1
        else:
            storey = storey % pow(10, c)
            c -= 1
            result += div
    
    return result
