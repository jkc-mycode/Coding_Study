import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if 0 <= X < n and 0 <= Y < m and maps[X][Y] == 0 and maps[X][Y] != -1:
                q.append((X, Y))
                maps[X][Y] = maps[x][y] + 1


m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            q.append((i, j))

bfs()

for i in maps:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    result = max(result, max(i))

print(result-1)