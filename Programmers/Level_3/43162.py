from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for idx, c in enumerate(computers):
        items = deque()

        if not visited[idx]:
            visited[idx] = True
            for i, con in enumerate(c):
                if i != idx and con == 1 and not visited[i]:
                    items.append(i)

            while items:
                item = items.popleft()
            
                if not visited[item]:
                    for j, con in enumerate(computers[item]):
                        if j != item and con == 1 and not visited[j]:
                            items.append(j)

                visited[item] = True

            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))