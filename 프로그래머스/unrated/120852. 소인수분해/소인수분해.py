def solution(n):
    value = []
    for i in range(2, n+1):
        count = 0
        for j in range(2, i+1):
            if count > 1:
                break
            if i%j==0:
                count += 1
        if count == 1 and n%i==0:
            value.append(i)
            
    return value
                
        
        
            
    
    