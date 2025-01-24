import heapq

def solution(scoville, K):
    scoville.sort()
    heapq.heapify(scoville)
    result = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        scv_1 = heapq.heappop(scoville)
        scv_2 = heapq.heappop(scoville)
        
        new_scv = scv_1 + (scv_2 * 2)
        heapq.heappush(scoville, new_scv)
        result += 1
    
    return result