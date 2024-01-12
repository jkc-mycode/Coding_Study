import sys

n = int(input())
data = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

count_val = [1 for i in range(n)]

for i in range(len(data)):
    for j in range(len(data)):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count_val[i] += 1

print(*count_val)