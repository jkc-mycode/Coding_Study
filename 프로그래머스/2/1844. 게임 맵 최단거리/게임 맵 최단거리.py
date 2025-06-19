from collections import deque

def solution(maps):
    result = 0
    dist = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    n, m = len(maps[0]), len(maps)
    queue = deque([[0, 0, 1]])
    visited = [[0] * n for _ in range(m)]
    visited[0][0] = 1
    
    while queue:
        x, y, value = queue.popleft()
        
        if x == m-1 and y == n-1:
            return value
        
        for d in dist:
            dx, dy = x + d[0], y + d[1]
            
            if 0 <= dx < m and 0 <= dy < n and visited[dx][dy] == 0 and maps[dx][dy] == 1:
                queue.append([dx, dy, value + 1])
                visited[dx][dy] = 1
    
    return -1
            