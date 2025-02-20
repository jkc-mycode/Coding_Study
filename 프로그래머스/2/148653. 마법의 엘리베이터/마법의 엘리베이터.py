def solution(storey):
    result = 0
    c = len(str(storey)) - 1
    
    while storey > 0:
        div = storey // pow(10, c)
        if div > 5:
            storey = pow(10, c+1) - storey
            result += 1
        elif div == 5:
            if storey == 5:
                result += 5
                break
            elif int(str(storey)[1]) >= 5:
                storey = pow(10, c+1) - storey
                result += 1
            else:
                storey = storey % pow(10, c)
                c -= 1
                result += div 
        else:
            storey = storey % pow(10, c)
            c -= 1
            result += div
    
    return result