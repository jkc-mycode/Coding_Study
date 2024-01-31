from collections import deque
import copy
import sys
input = sys.stdin.readline

def bfs(a, b, c):
    q = deque()
    q.append((a, b, c))

    while q:
        x, y, z = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]
        
        for i in range(4):
            X, Y = x + d[i][0], y + d[i][1]
            if 0 <= X < n and 0 <= Y < m:
                # X, Y 위치가 벽이고 벽파괴 기회를 사용하지 않은 경우
                # 벽을 부수고 이동
                # 이때부터는 더이상 벽을 파괴하지 못함
                if maps[X][Y] == 1 and z == 0:
                    visited[X][Y][1] = visited[x][y][0] + 1
                    q.append((X, Y, 1))
                # X, Y 위치가 벽이 아니고 아직 방문하지 않은 곳인 경우
                if maps[X][Y] == 0 and visited[X][Y][z] == 0:
                    visited[X][Y][z] = visited[x][y][z] + 1
                    q.append((X, Y, z))
    return -1


n, m = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(n)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# 3차원 리스트 사용
# [x][y][z]에서 z는 
# (앞으로 벽을 부쉴 수 있는 경로, 앞으로 벽을 부수지 못하는 경로)
# z의 (a, b) a와 b는 별도의 세계라고 생각하면 된다.
# a와 b 경로가 독립적으로 퍼진다고 생각
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

# maps의 사이즈가 1이라면 어떤 무조건 1이 출력되기에
# 복잡한 연산에 들어가기 전에 종료
if n == 1 and m == 1:
    print(1)
    exit()

print(bfs(0, 0, 0))