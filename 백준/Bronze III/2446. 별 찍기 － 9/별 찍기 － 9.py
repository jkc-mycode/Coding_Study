n = int(input())
value = 2 * n - 1
op = -2
space = value

for i in range(2 * n - 1):
    print(' ' * int((space - value)/2), end="")
    print('*' * value)
    if value == 1:
        op = 2
    value += op