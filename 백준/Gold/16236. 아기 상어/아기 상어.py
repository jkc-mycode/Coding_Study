from collections import deque
import sys
input = sys.stdin.readline

# 1. 아기 상어가 먹을 수 있는 물고기 중 가장 가까운 물고기를 선택
# 2. 아기 상어의 위치 기준으로 먹을 수 있는 물고기까지의 거리(시간)와 위치를 리스트에 넣음
# 3. 상하좌우 중 0(빈칸)이 아니면서 아기 상어보다 작은 값이면 거리 증가
# 4. 크기가 같으면 그냥 무시하고 거리 증가


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited = [[0] * n for _ in range(n)]
    visited[a][b] = 1
    cand = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            X, Y = x + d[i][0], y + d[i][1]

            if  0 <= X < n and 0 <= Y < n and visited[X][Y] == 0:
                if maps[X][Y] < baby and maps[X][Y] != 0:
                    visited[X][Y] = visited[x][y] + 1
                    cand.append((visited[X][Y] - 1, X, Y))
                elif maps[X][Y] == baby:
                    visited[X][Y] = visited[x][y] + 1
                    q.append((X, Y))
                elif maps[X][Y] == 0:
                    visited[X][Y] = visited[x][y] + 1
                    q.append((X, Y))
    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = 0, 0
baby = 2
fish = 0
time = 0

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            start_x, start_y = i, j


while True:
    maps[start_x][start_y] = baby
    cand = deque(bfs(start_x, start_y))

    if not cand:
        break
    
    # 시간, 위치
    t, x, y = cand.popleft()

    time += t
    fish += 1

    if baby == fish:
        baby += 1
        fish = 0
    
    maps[start_x][start_y] = 0
    start_x, start_y = x, y


print(time)

