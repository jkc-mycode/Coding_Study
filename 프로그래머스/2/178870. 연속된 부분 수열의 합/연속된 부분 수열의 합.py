def solution(sequence, k):
    result = []
    start = 0
    cur_sum = 0
    
    for end in range(len(sequence)):
        cur_sum += sequence[end]
        while cur_sum > k and start <= end:
            cur_sum -= sequence[start]
            start += 1
        
        if cur_sum == k:
            result.append([start, end])
            
    result.sort(key=lambda x: (x[1]-x[0], x[0]))
    
    return result[0]