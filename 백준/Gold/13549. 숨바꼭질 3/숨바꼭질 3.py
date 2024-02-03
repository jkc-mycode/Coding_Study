
# 가중치 별로 다른 연산을 해줘야 한다.
# [x, -1, 1] 일 때 각각의 가중치는  [0, 1, 1]이기 때문에
# x*2연산일 때는 appendleft 연산을 해줘야 한다.
# 심지어 가중치가 적은 것부터 우선적으로 큐에 넣어줘야 한다.
# 그리고 다른 가중치에 의해서 -와 +사이에도 순서가 생긴다.
# 9 13
# + - 순서인 경우 4, ( 9->10->11->12->13)
# - + 순서인 경우 3이 나옵니다. (9->8->7->14->13)

from collections import deque

def bfs(n, k):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        d = [x, -1, 1]

        if x == k:
            return maps[x]

        for i in range(3):
            X = x + d[i]
            if 0 <= X < 100001 and maps[X] == -1:
                if i == 0:
                    maps[X] = maps[x]
                    q.appendleft(X)
                else:
                    maps[X] = maps[x] + 1
                    q.append(X)
                

n, k = map(int, input().split())
maps = [-1] * 100001
maps[n] = 0


print(bfs(n, k))
