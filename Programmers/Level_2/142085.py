import heapq

def solution(n, k, enemy):
    answer, enemyAmount = 0, 0
    heap = []
    
    for e in enemy:
        heapq.heappush(heap, (-e, e))
        enemyAmount += e
        
        if enemyAmount > n:
            if k == 0:
                break
            enemy_max = heapq.heappop(heap)
            n += enemy_max[1]
            k -= 1
        
        answer += 1
    
    return answer