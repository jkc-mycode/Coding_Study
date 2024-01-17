import sys
sys.setrecursionlimit(3000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m: return False
    if maps[x][y] == 1:
        maps[x][y] = 0
        dfs(x+1, y)  # 상
        dfs(x-1, y)  # 하
        dfs(x, y-1)  # 좌
        dfs(x, y+1)  # 우
        return True
    return False


t = int(input())
bugs_num = []
for _ in range(t):
    m, n, k = map(int, input().split())

    maps = [[0] * (m) for _ in range(n)]
    bugs = 0

    for i in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                bugs += 1

    bugs_num.append(bugs)

for i in bugs_num:
    print(i)