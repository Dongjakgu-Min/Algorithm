def solution(cacheSize, cities):
    answer = 0
    cache = {}
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for idx, c in enumerate(cities):
        c = c.upper()
        if c not in cache:
            if len(cache) == cacheSize:
                del cache[min(cache, key=lambda k: (cache[k][1], cache[k][0]))]
            
            cache[c] = [0, idx]
            answer += 5
        else:
            cache[c][0] += 1
            cache[c][1] = idx
            answer += 1
    
    return answer

print(solution(5, ["Jeju", "Jeju", "Jeju"]))