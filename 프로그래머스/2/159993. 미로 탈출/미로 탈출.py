from collections import deque

def find_location(maps, location):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == location:
                return (i, j)

def bfs(maps, start, goal):
    row, col = len(maps), len(maps[0])
    visited = [[False] * col for _ in range(row)]
    path_dict = {start: None}
    queue = deque([start])
    dist = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        if goal == (x, y):
            path = []
            while path_dict[(x, y)] is not None:
                path.append((x, y))
                x, y = path_dict[(x, y)]
            return path[::-1]
        
        if not visited[x][y]:
            visited[x][y] = True
            for dx, dy in dist:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                    if maps[nx][ny] != 'X':
                        queue.append((nx, ny))
                        path_dict[(nx, ny)] = (x, y)
    return None

def solution(maps):
    maps = [list(m) for m in maps]
    start = find_location(maps, 'S')
    lever = find_location(maps, 'L')
    goal = find_location(maps, 'E')
    
    start_to_lever = bfs(maps, start, lever)
    lever_to_goal = bfs(maps, lever, goal)
    
    if start_to_lever == None or lever_to_goal == None:
        return -1
    else:
        return len(start_to_lever) + len(lever_to_goal)
