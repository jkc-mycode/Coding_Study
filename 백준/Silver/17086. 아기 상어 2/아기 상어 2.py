from collections import deque
import sys
input = sys.stdin.readline


def bfs(a, b):
    q = deque()
    q.append((a, b))

    visited = [[0] * m for _ in range(n)]
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        
        for i in range(8):
            X, Y = x + d[i][0], y + d[i][1]
            if 0 <= X < n and 0 <= Y < m and visited[X][Y] == 0:
                if maps[X][Y] == 0:
                    q.append((X, Y))
                    visited[X][Y] = visited[x][y] + 1

                if maps[X][Y] == 1:
                    safe.append(visited[x][y])
                    return


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
safe = [0]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            bfs(i, j)
            
print(max(safe))
