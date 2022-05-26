from itertools import combinations
from collections import Counter

def solution(orders, course):
    comb_list = []

    for order in orders:
        order = sorted(order)
        for c in course:
            comb_list += combinations(order, c)

    ct = Counter(comb_list).most_common()

    answer, hash = [], {}
    for k, v in ct:
        if len(k) not in hash.keys() or hash[len(k)] == v:
            if v <= 1:
                break
            answer.append(''.join(k))
            hash[len(k)] = v

    return sorted(answer)

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))