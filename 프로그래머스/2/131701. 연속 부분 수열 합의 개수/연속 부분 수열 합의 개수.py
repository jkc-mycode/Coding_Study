def solution(elements):
    list_set = set()
    for i in range(2, len(elements)):
        for j in range(len(elements)):
            if j + i >= len(elements):
                list_set.add(sum(elements[j:] + elements[:(j+i)%len(elements)]))
            else:
                list_set.add(sum(elements[j:(j+i)%len(elements)]))
    
    list_set = list_set.union(set(elements))
    list_set.add(sum(elements))
    
    return len(list_set)