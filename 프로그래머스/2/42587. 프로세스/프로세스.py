from collections import deque

def solution(priorities, location):
    queue = deque(list([i, priorities[i]] for i in range(len(priorities))))
    result = 0
    
    while len(queue) > 1:
        wait_process = queue.popleft()
        max_process = max(queue, key=lambda x: x[1])
        
        if wait_process[1] < max_process[1]:
            queue.append(wait_process)
        else:
            result += 1
            if wait_process[0] == location:
                return result
    return result + 1