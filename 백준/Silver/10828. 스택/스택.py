import sys

input_list = []
n = int(input())
for i in range(n):
    input_list.append(list(map(str, sys.stdin.readline().split())))

stack = []
for i in input_list:
    if i[0] == "push":
        stack.append(int(i[1]))
    elif i[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif i[0] == "size":
        print(len(stack))
    elif i[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif i[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
        