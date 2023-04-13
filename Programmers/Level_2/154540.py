from collections import deque

def solution(maps):
    answer = []
    split_map = []
    map_check = []
    for m in maps:
        split_map.append(list(m))
        map_check.append([False for _ in range(len(split_map[0]))])
        
    for i, m in enumerate(split_map):
        for j, elem in enumerate(m):
            q = deque()
            point = 0
            
            q.append((j, i))
            while (q):
                x, y = q.popleft()
                
                if split_map[y][x] == 'X' or map_check[y][x]:
                    continue
                else:
                    map_check[y][x] = True
                    point += int(split_map[y][x])
                    if x > 0 and not map_check[y][x - 1]:
                        q.append((x - 1, y))
                    if y > 0 and not map_check[y - 1][x]:
                        q.append((x, y - 1))
                    if x < len(split_map[0]) - 1 and not map_check[y][x + 1]:
                        q.append((x + 1, y))
                    if y < len(split_map) - 1 and not map_check[y + 1][x]:
                        q.append((x, y + 1))
                        
            if point != 0:
                answer.append(point)
                
    if len(answer) == 0:
        answer.append(-1)
    
    answer = sorted(answer)
    
    return answer