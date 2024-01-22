import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    visited[v] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                dis[i] = dis[v] + 1
                if dis[i] == k:
                    result.append(i)
                    

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dis = [0] * (n+1)
result = []

for i in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(x)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)