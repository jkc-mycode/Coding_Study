import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

count = 1
def dfs(r):
    global count
    visited[r] = count
    for i in graph[r]:
        if visited[i] == 0:
            count += 1
            dfs(i)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(r)
for i in visited[1:]:
    print(i)