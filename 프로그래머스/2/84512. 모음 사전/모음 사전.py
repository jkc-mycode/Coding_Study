alpha = ['A', 'E', 'I', 'O', 'U']
result = []

def dfs(cur):
    if len(cur) > 5:
        return
    result.append(cur)
    
    for a in alpha:
        dfs(cur + a)

def solution(word):
    dfs("")
    return result.index(word)
    