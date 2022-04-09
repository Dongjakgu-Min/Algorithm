from tabnanny import check


def solution(places):
    answer = []
    edited_p = []

    for p in places:
        temp = ['XXXXXXX']
        for l in p:
            temp.append('X' + l + 'X')
        temp.append('XXXXXXX')
        edited_p.append(temp)


    for p, line in enumerate(edited_p):
        check = 1
        for i, chars in enumerate(line):
            if i > 0 and i < 6:
                for j, c in enumerate(chars):
                    if c == 'P' and j > 0 and j < 6:
                        if 'P' == line[i - 1][j] or 'P' == line[i + 1][j] or 'P' == line[i][j - 1] or 'P' == line[i][j + 1]:
                            check = 0
                            break
                        if 'P' == line[i - 1][j - 1]:
                            if not ('X' == line[i - 1][j] and 'X' == line[i][j - 1]):
                                check = 0
                                break
                        if 'P' == line[i - 1][j + 1]:
                            if not ('X' == line[i - 1][j] and 'X' == line[i][j + 1]):
                                check = 0
                                break
                        if 'P' == line[i + 1][j - 1]:
                            if not ('X' == line[i + 1][j] and 'X' == line[i][j - 1]):
                                check = 0
                                break
                        if 'P' == line[i + 1][j + 1]:
                            if not ('X' == line[i + 1][j] and 'X' == line[i][j + 1]):
                                check = 0
                                break
                    if c == 'O' and j > 0 and j < 6:
                        if 'P' == line[i][j - 1] and 'P' == line[i][j + 1]:
                            check = 0
                            break
                        if 'P' == line[i - 1][j] and 'P' == line[i + 1][j]:
                            check = 0
                            break
            if check < 1:
                break
        answer.append(check)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))