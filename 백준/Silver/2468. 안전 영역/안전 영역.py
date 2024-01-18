import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(20000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n: return False
    if temp[x][y] != 0:
        temp[x][y] = 0
        dfs(x+1, y)  #상
        dfs(x-1, y)  #하
        dfs(x, y-1)  #좌
        dfs(x, y+1)  #우
        return True
    return False


n = int(input())
maps = []
max_height = 0
water_height = 0
count_list = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

for i in maps:
    if max_height < max(i):
        max_height = max(i)


for i in range(0, max_height+1):
    temp = copy.deepcopy(maps)
    
    for j in range(n):
        for k in range(n):
            if temp[j][k] <= i:
                temp[j][k] = 0
    count = 0
    for j in range(n):
        for k in range(n):
            if dfs(j, k) == True:
                count += 1
    count_list.append(count)

print(max(count_list))

