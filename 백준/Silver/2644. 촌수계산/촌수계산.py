import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v):
    visited[v] = 1
    for i in maps[v]:
        if visited[i] == 0:
            result[i] = result[v] + 1
            dfs(i)

n = int(input())
a, b = map(int, input().split())

maps = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = [0] * (n+1)

m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    maps[x].append(y)
    maps[y].append(x)

dfs(a)

if result[b] == 0: print(-1)
else: print(result[b])