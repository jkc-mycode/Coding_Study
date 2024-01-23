import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            X, Y = x + dx[i], y + dy[i]

            if 0 <= X < n and 0 <= Y < m and maps[X][Y] == 1:
                q.append((X, Y))
                maps[X][Y] = maps[x][y] + 1


n, m = map(int, input().split())
maps = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    maps.append(list(map(int, input().rstrip())))

bfs(0, 0)
print(maps[n-1][m-1])