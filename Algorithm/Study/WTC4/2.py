def solution(logs):
    answer = 0
    for i in range(1, len(logs), 2):
        start, end = logs[i].split(':'), logs[i - 1].split(":")
        hour = (int(start[0]) - int(end[0])) * 60
        minute = int(start[1]) - int(end[1])
        total = hour + minute

        if total > 105:
            total = 105
        elif total < 5:
            total = 0

        answer += total

    h = str(answer // 60) if answer // 60 > 9 else '0' + str(answer // 60)
    m = str(answer % 60)

    return h + ':' + m