T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    pre = [[i for i in range(1, n+1)]]

    if k == 1:
        print(sum([j for j in range(1, n+1)]))
    else:
        for j in range(1, k):
            pre.append([])
            for l in range(n):
                pre[j].append(sum(pre[j-1][:l+1]))
        print(sum(pre[k-1]))
