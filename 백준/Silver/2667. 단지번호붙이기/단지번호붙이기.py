import sys

home = 0  # 한 단지내에 있는 집의 수
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n: return False
    if map[x][y] == 1:  # x,y 에 집이 있는 경우
        global home
        home += 1  # 집 수 증가
        map[x][y] = 0  # 체크한 좌표이기에 0으로 표시
        dfs(x, y+1)  # 상
        dfs(x, y-1)  # 하
        dfs(x-1, y)  # 좌
        dfs(x+1, y)  # 우
        return True
    return False
        

n = int(input())
map = [[int(j) for j in input()] for i in range(n)]

apart = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            apart.append(home)
            home = 0


print(len(apart))
apart.sort()
for i in apart:
    print(i)