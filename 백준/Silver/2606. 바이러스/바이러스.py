def dfs(v):
    global count
    count += 1
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


n = int(input())  # 정점의 수
m = int(input())  # 간선의 수
# 1번 컴퓨터와 연결된 컴퓨터 수, 0부터하면 그냥 1까지 포함해서 count하기 때문에
count = -1  

graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(1)
print(count)