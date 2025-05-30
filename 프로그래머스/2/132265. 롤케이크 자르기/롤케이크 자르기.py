from collections import Counter

def solution(topping):
    result = 0
    me = Counter(topping)
    bro = set()
    
    for t in topping:
        me[t] -= 1
        if me[t] == 0: me.pop(t)
        bro.add(t)
        if len(me) == len(bro):
            result += 1
    
    return result
        