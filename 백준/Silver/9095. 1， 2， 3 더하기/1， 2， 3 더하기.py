n = int(input())
input_data = [int(input()) for _ in range(n)]

for i in input_data:
    d = [0] * (i+1)
    for j in range(1, i+1):
        if j == 1:
            d[j] = 1
        elif j == 2:
            d[j] = 2
        elif j == 3:
            d[j] = 4
        else:
            d[j] = d[j-1] + d[j-2] + d[j-3]
    print(d[j])
