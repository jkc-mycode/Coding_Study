def solution(cacheSize, cities):
    cache = {}
    cache_key = []
    result = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            result += 1
            cache_key.remove(city)
            cache_key.append(city)
        else:
            result += 5
            if cacheSize > 0:
                if len(cache_key) >= cacheSize:
                    oldest_city = cache_key.pop(0)
                    del cache[oldest_city]
            cache[city] = True
            cache_key.append(city)

    return result
            