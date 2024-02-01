from collections import deque
import copy
import sys
input = sys.stdin.readline

def bfs(a, b, color, maps):
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            X, Y = x + d[i][0], y + d[i][1]
            if 0 <= X < n and 0 <= Y < n and maps[X][Y] == color:
                global count
                count += 1
                q.append((X, Y))
                maps[X][Y] = '0'


n = int(input())
maps = [list(map(str, input().rstrip())) for _ in range(n)]
maps_gb = copy.deepcopy(maps)
r, g, b = [], [], []
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

count = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'R':
            bfs(i, j, 'R', maps)
            r.append(count)
        elif maps[i][j] == 'G':
            bfs(i, j, 'G', maps)
            g.append(count)
        elif maps[i][j] == 'B':
            bfs(i, j, 'B', maps)
            b.append(count)
        count = 0
print(len(r) + len(g) + len(b), end=" ")

r, g, b = [], [], []
for i in range(n):
    for j in range(n):
        if maps_gb[i][j] == 'R':
            maps_gb[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if maps_gb[i][j] == 'G':
            bfs(i, j, 'G', maps_gb)
            g.append(count)
        elif maps_gb[i][j] == 'B':
            bfs(i, j, 'B', maps_gb)
            b.append(count)
        count = 0

print(len(r) + len(g) + len(b))