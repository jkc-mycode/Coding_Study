def solution(land):
    a,b,c,d = land[0]
    
    for i in land[1:]:
        e,f,g,h = a,b,c,d
        a,b,c,d = i
        
        a += max(f,g,h)
        b += max(e,g,h)
        c += max(e,f,h)
        d += max(e,f,g)
    
    return max(a, b, c, d)