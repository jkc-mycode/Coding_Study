from collections import deque

# BFS 활용
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0, 1)])
    dist = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, value = queue.popleft()
        
        if x == n-1 and y == m-1:
            return value
        
        for d in dist:
            nx, ny = x + d[0], y + d[1]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, value+1))
    return -1
