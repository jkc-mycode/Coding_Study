def solution(citations):
    result = 0
    citations.sort()
    
    for i in range(len(citations)):
        citations_length = len(citations[i:])
        if citations_length <= citations[i]:
            result = citations_length
            break
    
    return result