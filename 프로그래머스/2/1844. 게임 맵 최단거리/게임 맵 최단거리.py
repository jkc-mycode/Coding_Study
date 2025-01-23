from collections import deque

def solution(maps):
    row, col = len(maps), len(maps[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(0, 0)])
    dist = [[0] * col for _ in range(row)]
    dist[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            
            if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    
    if dist[row-1][col-1] == 0:
        return -1
    else:
        return dist[row-1][col-1]