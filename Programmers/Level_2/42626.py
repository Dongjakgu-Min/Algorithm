import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        min_first = heapq.heappop(scoville)
        min_second = heapq.heappop(scoville)
        answer += 1

        heapq.heappush(scoville, min_first + min_second * 2)

        if len(scoville) == 1:
            break

    if scoville[0] < K:
        return -1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))