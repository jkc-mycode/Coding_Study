import sys
input = sys.stdin.readline


n = int(input())
t_list = []
p_list = []
dp = [0 for i in range(n+1)]


for _ in range(n):
    a, b = map(int, input().split())
    t_list.append(a)
    p_list.append(b)


for i in range(n):
    for j in range(i+t_list[i], n+1):
        if dp[j] < dp[i] + p_list[i]:
            dp[j] = dp[i] + p_list[i]

print(dp[-1])