from collections import deque

def solution(maps: list):
    visited = [[False for _ in range(len(maps[0]) + 2)] for _ in range(len(maps) + 2)]
    level = [[0 for _ in range(len(maps[0]) + 2)] for _ in range(len(maps) + 2)]
    goal = (len(maps), len(maps[0]))

    def check_map(x, y):
        if not visited[x + 1][y] and maps[x + 1][y] == 1:
            next_pos.append((x + 1, y))
            level[x + 1][y] = level[x][y] + 1
            visited[x + 1][y] = True
        if not visited[x - 1][y] and maps[x - 1][y] == 1:
            next_pos.append((x - 1, y))
            level[x - 1][y] = level[x][y] + 1
            visited[x - 1][y] = True
        if not visited[x][y + 1] and maps[x][y + 1] == 1:
            next_pos.append((x, y + 1))
            level[x][y + 1] = level[x][y] + 1
            visited[x][y + 1] = True
        if not visited[x][y - 1] and maps[x][y - 1] == 1:
            next_pos.append((x, y - 1))
            level[x][y - 1] = level[x][y] + 1
            visited[x][y - 1] = True

    for i in range(len(maps)):
        maps[i].insert(0, 0)
        maps[i].append(0)

    maps.insert(0, [0 for _ in range(len(maps[0]))])
    maps.append([0 for _ in range(len(maps[0]))])

    next_pos = deque()
    next_pos.append((1, 1))
    visited[1][1] = True

    while next_pos:
        cur = next_pos.popleft()

        print(cur)

        if visited[goal[0]][goal[1]]:
            break

        check_map(cur[0], cur[1])

    if not visited[goal[0]][goal[1]]:
        return -1

    return level[goal[0]][goal[1]] + 1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))