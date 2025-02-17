def solution(queue1, queue2):
    result = 0
    q1 = sum(queue1)
    q2 = sum(queue2)
    q_sum = (q1 + q2) / 2
    i, j = 0, 0
    
    for k in range(len(queue1)*10):
        if q1 == q2:
            break
        if q1 < q_sum:
            q1 += queue2[j]
            q2 -= queue2[j]
            queue1.append(queue2[j])
            j += 1
        else:
            q1 -= queue1[i]
            q2 += queue1[i]
            queue2.append(queue1[i])
            i += 1
        result += 1
    
    if q1 != q2:
        return -1
        
    return result