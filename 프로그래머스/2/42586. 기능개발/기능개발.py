from collections import deque

def solution(progresses, speeds):
    result = []
    prog_queue = deque(progresses)
    speed_queue = deque(speeds)
    
    while prog_queue:
        count = 0
        while prog_queue and prog_queue[0] >= 100:
            prog_queue.popleft()
            speed_queue.popleft()
            count += 1
            
        if count != 0:
            result.append(count)
        
        for i in range(len(prog_queue)):
            prog_queue[i] += speed_queue[i]
        
    
    return result
        