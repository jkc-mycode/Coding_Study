def solution(n):
    result = []
    matrix = [[0] * n for _ in range(n)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            x += dx[i % 3]
            y += dy[i % 3]
            matrix[x][y] = num
            num += 1
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                result.append(matrix[i][j])
    
    return result