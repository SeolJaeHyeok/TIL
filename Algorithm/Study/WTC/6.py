# 우테코 2기 6번
def solution(tickets, logs):
    answer = []

    prev_time = 0
    for i in range(len(logs)):
        log = logs[i].split()
        if log[1] == 'request':
            tmp = log[2].split(':')
            curTime = int(tmp[1]) * 60 + int(tmp[2])
            if curTime > prev_time + 60:
                answer.append(log[0])
                prev_time = curTime
        else:
            answer.remove(log[0])

    answer.sort()
    return answer


print(solution(2000, [
    "woni request 09:12:29",
    "brown request 09:23:11",
    "brown leave 09:23:44",
    "milk request 09:25:29",
    "choo request 09:26:27",
    "jason request 09:33:51",
    "jun request 09:33:56",
    "cu request 09:34:02",
]))