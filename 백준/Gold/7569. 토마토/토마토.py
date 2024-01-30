from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        a, b, c = q.popleft()
        for i in d:
            A, B, C = a + i[0], b + i[1], c + i[2]
            if 0 <= A < h and 0 <= B < n and 0 <= C < m and maps[A][B][C] == 0:
                maps[A][B][C] = maps[a][b][c] + 1
                q.append([A, B, C])


m, n, h = map(int, input().split())
maps = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
days = 0

d = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

count = 0
for i in maps:
    for j in i:
        for k in j:
            if k == 0:
                count += 1
if count == 0:
    print(0)
    exit()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if maps[i][j][k] == 1:
                q.append([i, j, k])

bfs()

for i in maps:
    for j in i:
        days = max(days, *j)

for i in maps:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()

print(days-1)


