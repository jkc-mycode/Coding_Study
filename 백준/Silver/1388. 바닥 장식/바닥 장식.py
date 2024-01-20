import sys
input = sys.stdin.readline

def dfs(x, y):
    if maps[x][y] == '-':
        maps[x][y] = 0
        for a in [1, -1]:
            Y = y + a
            if (0 < Y < m) and maps[x][Y] == '-':
                dfs(x, Y)
        
    if maps[x][y] == '|':
        maps[x][y] = 0
        for b in [1, -1]:
            X = x + b
            if (0 < X < n) and maps[X][y] == '|':
                dfs(X, y)
        

n, m = map(int, input().split())
maps = []
count = 0

for i in range(n):
    maps.append(list(input().rstrip()))

for i in range(n):
    for j in range(m):
        if maps[i][j] == '-' or maps[i][j] == '|':
            dfs(i, j)
            count += 1

print(count)