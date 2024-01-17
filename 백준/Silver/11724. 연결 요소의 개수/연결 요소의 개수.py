import sys
sys.setrecursionlimit(3000)

def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and maps[v][i]:
            dfs(i)
    

n, m = map(int, input().split())
maps = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    maps[a][b] = maps[b][a] = 1

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)