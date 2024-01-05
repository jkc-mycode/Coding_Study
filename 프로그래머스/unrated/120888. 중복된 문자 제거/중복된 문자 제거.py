def solution(my_string):
    results = []
    for i in my_string:
        if i not in results:
            results.append(i)
    return "".join(results)
        
            
            