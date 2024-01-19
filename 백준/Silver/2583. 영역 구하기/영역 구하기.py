import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n: return False
    if maps[x][y] == 0:
        global count
        count += 1
        maps[x][y] = 1
        dfs(x+1, y)  # 상
        dfs(x-1, y)  # 하
        dfs(x, y-1)  # 좌
        dfs(x, y+1)  # 우
        return True
    return False


m, n, k = map(int, input().split())
maps = [[0] * n for _ in range(m)]
area = []

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            maps[y][x] = 1

count = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j):
            area.append(count)
            count = 0

print(len(area))
print(*sorted(area))