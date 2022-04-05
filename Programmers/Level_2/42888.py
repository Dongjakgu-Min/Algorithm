def solution(record):
    answer = []
    user = {}

    for command in record:
        if command[0] != 'L':
            cmd, uid, name = command.split(' ')
            user[uid] = name

    for command in record:
        cmd = command.split(' ')
        if cmd[0] == 'Leave':
            answer.append('{0}님이 나갔습니다.'.format(user[cmd[1]]))
        elif cmd[0] == 'Enter':
            answer.append('{0}님이 들어왔습니다.'.format(user[cmd[1]]))
            
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))