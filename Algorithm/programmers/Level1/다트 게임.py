# 2018 카카오 블라인드 테스트 [1차] 다트 게임
def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'G')
    for i in dartResult:
        if i.isdigit() or i == 'G':
            if i == 'G':
                steps = 10
            else:
                steps = int(i)
        elif i == 'S':
            steps = steps ** 1
            answer.append(steps)
            continue
        elif i == 'D':
            steps = steps ** 2
            answer.append(steps)
            continue
        elif i == 'T':
            steps = steps ** 3
            answer.append(steps)
            continue
        elif i == '*':
            if len(answer) <= 1:
                answer[0] = answer[0] * 2
            else:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
        elif i == '#':
            answer[-1] = answer[-1] * -1

    return sum(answer)