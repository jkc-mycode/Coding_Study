def solution(cacheSize, cities):
    result = 0
    cache = {}
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for i in range(len(cities)):
        city = cities[i].lower()
        if cache.get(city) != None:
            result += 1
        else:
            result += 5
            if len(cache) == cacheSize:
                temp_key = min(cache, key=cache.get)
                cache.pop(temp_key)
        cache[city] = i
    
    return result