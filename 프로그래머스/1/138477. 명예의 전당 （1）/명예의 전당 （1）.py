def solution(k, score):
    result = []
    top_k = []
    
    for i in range(len(score)):
        top_k.append(score[i])
        top_k.sort(reverse=True)
        if len(top_k) > k:
            top_k.pop()
        result.append(top_k[-1])
    return result
            