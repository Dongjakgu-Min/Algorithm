from collections import deque

def solution(priorities, location):
    answer = 0
    temp = deque()
    max_val = max(priorities)

    for p in enumerate(priorities):
        temp.append(p)

    while True:
        doc = temp.popleft()
        
        if doc[1] < max_val:
            temp.append(doc)
        else:
            answer += 1
            if temp:
                max_val = max(temp, key=lambda x:x[1])
                max_val = max_val[1]

            if doc[0] == location:
                break

    return answer

print(solution(	[1, 1, 7, 1, 9, 1, 1], 1))