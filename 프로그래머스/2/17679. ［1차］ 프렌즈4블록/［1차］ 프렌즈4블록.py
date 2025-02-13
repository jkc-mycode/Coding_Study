def solution(m, n, board):
    result = 0
    list_board = []
    
    for i in range(m):
        list_board.append(list(board[i]))
    
    while True:
        temp = []
        for i in range(m-1):
            for j in range(n-1):
                if list_board[i][j] != "*" and list_board[i][j] == list_board[i][j+1] == list_board[i+1][j] == list_board[i+1][j+1]:
                    temp.append([i,j])
                    temp.append([i+1,j])
                    temp.append([i,j+1])
                    temp.append([i+1,j+1])
        for t in temp:
            list_board[t[0]][t[1]] = "*"

        for i in range(n):
            cols = []
            for j in range(m):
                if list_board[j][i] != "*":
                    cols.append(list_board[j][i])
            while len(cols) < m:
                cols.insert(0, "*");
            for j in range(m):
                list_board[j][i] = cols.pop(0)
        
        if len(temp) == 0:
            break
    
    for i in range(m):
        for j in range(n):
            if list_board[i][j] == "*":
                result += 1
    
    return result