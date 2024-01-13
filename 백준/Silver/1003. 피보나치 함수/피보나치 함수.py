n = int(input())

for _ in range(n):
    x = int(input())
    d = [0] * (x+2)
    for i in range(1, x+2):
        if i == 0:
            d[i] += 1
        elif i == 1:
            d[i] += 1
        else:
            d[i] = d[i-1] + d[i-2]
    if x == 0:
        print(1, 0)
    else:
        print(d[x-1], d[x])