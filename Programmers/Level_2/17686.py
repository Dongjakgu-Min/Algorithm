import re

def solution(files):
    name = {}

    for f in files:
        name[f] = {}
        name[f]['head'] = [re.search('^[a-zA-Z\s\-]+', f), re.findall('^[a-z,A-Z\s\-]+', f)]
        print(name[f]['head'][1])
        name[f]['number'] = [re.search('[1-9]+', f), re.findall('[0-9]+', f)]

    sorted_dict = [i[0] for i in sorted(name.items(), key=lambda item: (item[1]['head'][1][0].upper(), int(item[1]['number'][1][0])))]

    return sorted_dict

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", "F-15"]))
