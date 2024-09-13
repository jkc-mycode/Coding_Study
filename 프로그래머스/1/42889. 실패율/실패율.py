def solution(N, stages):
    result = []
    total = len(stages)
    
    for num in range(1, N+1):
        if total != 0:
            count = stages.count(num)
            result.append((num, count/total))
        else:
            result.append((num, 0))
        total -= count        
        
    result.sort(key = lambda x : (-x[1], x[0]))
    
    return list(i[0] for i in result)
        
                
                