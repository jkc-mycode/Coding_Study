def solution(wallpaper):
    width = len(wallpaper[0])
    height = len(wallpaper)
    x, y = [], []
    
    for i in range(height):
        for j in range(width):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    
    return min(x), min(y), max(x)+1, max(y)+1