def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    win_count = 0
    zero_count = 0
    
    for i in lottos:
        if i in win_nums:
            win_count += 1
        elif i == 0:
            zero_count += 1
    
    return [rank[win_count + zero_count], rank[win_count]]