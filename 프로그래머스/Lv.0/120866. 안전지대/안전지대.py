def solution(board):
    val = board
    count_1 = sum([1 for i in board for j in i if j == 1])
    temp = 0
    for i in range(len(val)):
        for j in range(len(val[0])):
            # if temp >= count_1: break
            if val[i][j] == 1:
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        nx = i+x
                        ny = j+y
                        
                        if 0 <= nx < len(val) and 0 <= ny < len(val) and val[nx][ny] != 1:
                            val[nx][ny] = "X" 
                    
    
    for i in val:
        print(i)
    return sum([1 for i in board for j in i if j == 0])
            
