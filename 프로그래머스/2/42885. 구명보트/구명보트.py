from collections import deque

def solution(people, limit):
    result = 0
    sorted_people = sorted(people, reverse=True)
    queue = deque(sorted_people)
    
    while queue:
        value = queue.popleft()
        if value <= limit:
            if queue and value + queue[-1] <= limit:
                value += queue.pop()
        result += 1
    
    return result
                