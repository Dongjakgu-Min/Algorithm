def solution(numbers, target):
    answer = 0
    tree = [0, numbers[0]]
    result = [0, numbers[0]]
    result_m = [0, -numbers[0]]

    for idx, e in enumerate(numbers[1:]):
        for _ in range(2 ** idx):
            tree.append(e)
            tree.append(-e)

    for i in range(1, len(numbers)):
        for j in range(2 ** (i), 2 ** (i + 1)):
            result.append(tree[j] + result[int(j / 2)])
            result_m.append(tree[j] + result_m[int(j / 2)])

    answer = result[-(2 ** (len(numbers) - 1)):].count(target) + result_m[-(2 ** (len(numbers) - 1)):].count(target)

    return answer

print(solution([1, 1, 1, 1, 1], 3))