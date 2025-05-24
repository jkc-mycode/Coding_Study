def solution(elements):
    ell = len(elements)
    list_set = set()
    
    for i in range(2, ell):
        for j in range(ell):
            if j + i >= ell:
                list_set.add(sum(elements[j:] + elements[:(j+i)%ell]))
            else:
                list_set.add(sum(elements[j:(j+i)%ell]))
    
    list_set = list_set.union(set(elements))
    list_set.add(sum(elements))
    
    return len(list_set)