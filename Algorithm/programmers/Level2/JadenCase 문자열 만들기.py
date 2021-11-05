def solution(s):
    s = s.split(' ')
    answer = []
    for char in s:
        tmp = ''
        for i in range(len(char)):
            if i == 0:
                tmp += char[i].upper()
            else:
                tmp += char[i].lower()
        answer.append(tmp)

    return ' '.join(answer)
