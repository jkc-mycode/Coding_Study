def solution(citations):
    result = 0
    citations.sort()
    
    for i in range(len(citations)):
        citations_len = len(citations[i:])
        if citations_len <= citations[i]:
            result = citations_len
            break
    
    return result
        