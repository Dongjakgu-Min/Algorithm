def solution(lottos, win_nums):
    zeros = lottos.count(0)
    lottos, win_nums = set(lottos), set(win_nums)
    result = len(list(lottos & win_nums))

    print(result)
    
    return [7 - result - zeros if 7 - result - zeros < 7 else 6, 7 - result if 7 - result < 7 else 6]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))