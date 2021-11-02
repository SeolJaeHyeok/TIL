def solution(s):
    answer = ''
    array = s.split(' ')
    count = 0
    for char in array:
        count += 1
        for i in range(len(char)):
            if i % 2 == 0:
                answer += char[i].upper()
            else:
                answer += char[i].lower()
        if count < len(array):
            answer += ' '

    return answer


def solution(s):
    answer = []

    for char in s.split(' '):
        word = ''
        for i in range(len(char)):
            c = char[i].upper() if i % 2 == 0 else char[i].lower()
            word += c
        answer.append(word)

    return ' '.join(answer)