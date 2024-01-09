def solution(score):
    val = [sum(i) for i in score]
    sorted_val = sorted(val, reverse=True)
    
    return [sorted_val.index(i) + 1 for i in val]
    