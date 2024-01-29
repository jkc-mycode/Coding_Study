import sys
import copy
from collections import deque
input = sys.stdin.readline

# 1. 무작위로 벽 3개를 세운다. (원본 maps에서)
# 2. 세워진 벽을 기반으로 바이러스 확산을 테스트한다. (깊은 복사를 통해 또 다른 테스트용 maps을 생성)
# 3. 안전 구역의 개수를 구한다.

def bfs():
    q = deque()
    # 매번 깊은 복사를 통해 세워진 벽에 의한 바이러스 확산을 테스트
    test_maps = copy.deepcopy(maps)

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                q.append((i, j))
    
    while q:
        x, y = q.popleft() 
        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if 0 <= X < n and 0 <= Y < m and test_maps[X][Y] == 0:
                q.append((X, Y))
                test_maps[X][Y] = 2  # 바이러스 확산
    
    # 테스트 맵에서 안전구역의 수를 센다.
    global result
    count = 0
    for i in range(n):
        for j in range(m):
            if test_maps[i][j] == 0:
                count += 1
    result = max(count, result)


def make_walls(count):
    # 벽이 3개 세워지면 bfs()로 바이러스 확산 테스트
    if count == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                make_walls(count+1)
                maps[i][j] = 0  # 원본 maps을 수정했다가 다시 복원 (다른 테스트를 하기 위해)


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

make_walls(0)

print(result)