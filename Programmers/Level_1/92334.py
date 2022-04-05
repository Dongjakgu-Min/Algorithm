def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    alert = [[] for _ in range(len(id_list))]
    
    report = set(report)
    for i in report:
        name, target = i.split(' ')
        alert[id_list.index(target)].append(name)

    for i in alert:
        if len(i) >= k:
            for j in i:
                answer[id_list.index(j)] += 1

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))