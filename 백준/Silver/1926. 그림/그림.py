import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or  y >= m: return False
    if maps[x][y] == 1:
        global count
        count += 1
        maps[x][y] = 0
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)
        return True
    return False

n, m = map(int, input().split())
maps = []
result = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

count = 0
for i in range(n):
    for j in range(m):
        count = 0
        if maps[i][j] == 1 and dfs(i, j):
            result.append(count)

print(len(result))
if len(result) == 0:
    print(0)
else:
    print(max(result))