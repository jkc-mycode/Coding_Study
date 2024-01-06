def solution(my_string):
    temp = my_string
    for i in my_string:
        if i.isalpha():
            temp = temp.replace(i, ' ')
    
    return sum(int(i) for i in temp.split(' ') if i.isdigit())
            