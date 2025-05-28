def solution(cacheSize, cities):
    result = 0
    count = 1
    cache = {}
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        norm_city = city.lower()
        if cache.get(norm_city) == None:
            if len(cache) == cacheSize:
                min_key = min(cache, key=cache.get)
                cache.pop(min_key)
            result += 5
        else:
            result += 1    
        cache[norm_city] = count
        count += 1
    
    return result