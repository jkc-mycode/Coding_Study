def solution(board, h, w):
    dh = [0, 1, 0, -1]
    dw = [1, 0, -1, 0]
    
    count = 0
    
    for i in range(len(dh)):
        new_h = h + dh[i]
        new_w = w + dw[i]
        if new_h >= 0 and new_h < len(board) and new_w >= 0 and new_w < len(board):
            if board[h][w] == board[new_h][new_w]:
                count += 1
    return count
            