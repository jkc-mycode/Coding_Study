from collections import deque

def dfs(v):
    # 재귀 활용
    visited_1[v] = 1
    print(v, end=" ")
    
    for i in range(1, n+1):
        # 방문기록이 없고, 인덱스에 값이 있다면(연결되어있다면)
        if visited_1[i] == 0 and graph[v][i]:
            dfs(i)

def bfs(v):
    # 큐 활용
    q = deque([v])
    visited_2[v] = 1

    while q:
        # 시작 위치를 업데이트하기 위해서
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            # 방문기록이 없고, 인덱스에 값이 있다면(연결되어있다면)
            if visited_2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited_2[i] = 1



n, m, v = map(int, input().split())  # 정점의 수, 간선의 수, 시작 정점

# 정점끼리의 연결 유무를 담을 2차원 리스트
# n+1은 편의상 0부터가 아니라 1부터로 맞추기 위해서 사용, 정점의 숫자(값)과 graph의 인덱스를 맞추기 위해
graph = [[0] * (n+1) for _ in range(n+1)]  
visited_1 = [0] * (n+1)
visited_2 = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)