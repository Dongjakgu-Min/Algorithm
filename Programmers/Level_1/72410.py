import re


def solution(new_id: str):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('[.]{3,}', '.', new_id)

    if new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[0:-1]

    if len(new_id) == 0:
        new_id = 'a'
    
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[0:-1]

    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

print(solution("=.="))