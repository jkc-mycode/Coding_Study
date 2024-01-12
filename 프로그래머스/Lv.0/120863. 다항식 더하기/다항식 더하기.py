def solution(polynomial):
    val = polynomial.split(" + ")
    x_sum = 0
    n_sum = 0
    
    for i in val:
        if i.isdigit():
            n_sum += int(i)
        else:
            if i == 'x' or i == '1x':
                x_sum += 1
            else:
                x_sum += int(i[:-1])
    
    if x_sum == 0 and n_sum == 0:
        return '0'
    elif x_sum == 0:
        return f'{n_sum}'
    elif x_sum == 1 and n_sum == 0:
        return 'x'
    elif x_sum == 1 and  n_sum != 0:
        return f'x + {n_sum}'
    elif x_sum != 0 and n_sum == 0:
        return f'{x_sum}x'
    else:
        return f'{x_sum}x + {n_sum}'
        