def solution(my_string):
    return ''.join([chr(ord(i)-32) if ord(i)>=95 else chr(ord(i)+32) for i in my_string])