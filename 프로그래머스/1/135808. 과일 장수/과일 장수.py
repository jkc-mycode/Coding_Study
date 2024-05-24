def solution(k, m, score):
    result = 0
    sorted_score = sorted(score, reverse=True)
    
    for i in range(0, len(score), m):
        if i + m <= len(score):
            result += min(sorted_score[i:i+m]) * m
            
    return result