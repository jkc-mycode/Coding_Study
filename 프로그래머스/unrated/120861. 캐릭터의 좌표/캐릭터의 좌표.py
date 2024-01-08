def solution(keyinput, board):
    x, y = 0, 0
    x_size, y_size = board[0]//2, board[1]//2
    
    for i in keyinput:
        if i == "left" and x > -x_size:
            x -= 1
        elif i == "right" and x < x_size:
            x += 1
        elif i == "up" and y < y_size:
            y += 1
        elif i == "down" and y > -y_size:
            y -= 1
        
    return [x, y]
            
    
        
