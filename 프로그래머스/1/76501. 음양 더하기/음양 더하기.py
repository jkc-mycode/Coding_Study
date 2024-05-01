def solution(absolutes, signs):
    result = 0;
    
    for i in range(len(signs)):
        if not signs[i]:
            absolutes[i] *= -1
    
    return sum(absolutes)