def solution(citations):
    result = []
    
    for i in range(max(citations)):
        if i > len(result): break
        result = list(filter(lambda x: x>=i, citations))
        
    return len(result)