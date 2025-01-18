def solution(n, words):
    n_dict = {i: 0 for i in range(1, n+1)}
    used_words = [words[0]]
    n_dict[1] += 1
    
    for i in range(1, len(words)):
        if words[i-1][-1] == words[i][0] and (words[i] not in used_words):
            n_dict[i%n+1] += 1
            used_words.append(words[i])
            continue
        return [i%n+1, n_dict[i%n+1]+1]
    
    return [0,0]
        