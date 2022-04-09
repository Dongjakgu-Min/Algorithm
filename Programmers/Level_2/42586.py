import math

def solution(progresses, speeds):
    answer = []
    remains = []

    for i, j in zip(progresses, speeds):
        remains.append([math.ceil((100 - i) / j), False])

    print(remains)

    for idx, work in enumerate(remains):
        if work[1] == False:
            answer.append(1)
            for i, day in enumerate(remains[idx + 1:]):
                if work[0] < day[0]:
                    break
                answer[-1] += 1
                remains[i + idx + 1][1] = True
            remains[idx][1] = True
            print(remains)
                

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))