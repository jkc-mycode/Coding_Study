def solution(elements):
    result = [i for i in elements]
    el_len = len(elements)
    
    for i in range(2, el_len):
        for j in range(el_len):
            if j+i < el_len:
                result.append(sum(elements[j:j+i]))
            else:
                temp = elements[j:] + elements[:(i+j)%el_len]
                result.append(sum(temp))
    
    result.append(sum(elements))
    return len(list(set(result)))