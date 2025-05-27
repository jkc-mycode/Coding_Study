from collections import deque

def solution(progresses, speeds):
    result = []
    queue = deque(progresses)
    speed_queue = deque(speeds)
    
    while queue:
        count = 0
        for i in range(len(queue)):
            queue[i] += speed_queue[i]
        
        while queue and queue[0] >= 100:
            queue.popleft()
            speed_queue.popleft()
            count += 1
        
        if count != 0:
            result.append(count)
        
    return result
        