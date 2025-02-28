from collections import deque

def solution(people, limit):
    result = 0
    queue = deque(sorted(people, reverse=True))
    
    while queue:
        cur = queue.popleft()
        if cur <= limit:
            if queue and cur + queue[-1] <= limit:
                cur += queue.pop()
        result += 1
    
    return result