def solution(hp):
    ants = {0:5, 1:3, 2:1}
    results = [0, 0, 0]

    for k, v in ants.items():
        results[k] = int(hp/v)
        hp = hp%v
    
    return sum(results)