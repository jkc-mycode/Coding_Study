def compress(arr, row, col, size):
    init = arr[row][col]
    all_same = True
    
    for i in range(row, row + size):
        for j in range(col, col + size):
            if arr[i][j] != init:
                all_same = False
                break
        if not all_same:
            break
    
    if all_same:
        return (0, 1) if init == 1 else (1, 0)
    else:
        half = size // 2
        top_left = compress(arr, row, col, half)
        top_right = compress(arr, row, col+half, half)
        bottom_left = compress(arr, row+half, col, half)
        bottom_right = compress(arr, row+half, col+half, half)
        
        return (top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0], top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1])

def solution(arr):
    n = len(arr)
    result = compress(arr, 0, 0, n)
    return [result[0], result[1]]