def solution(board, moves):
    result = 0
    bucket = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                bucket.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(bucket) > 1 and bucket[-1] == bucket[-2]:
            del bucket[-1]
            del bucket[-1]
            result += 2
        
    return result