def solution(s):
    result = []
    for word in s.split(" "):
        temp = ''
        for j in range(len(word)):
            if j % 2 == 0: 
                temp += word[j].upper()
            else:
                temp += word[j].lower()
        result.append(temp)
        
    return " ".join(result)