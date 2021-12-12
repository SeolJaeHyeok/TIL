from collections import deque


def solution(s):
    answer = []
    q = deque()

    for i in range(len(s)):
        q.append(s[i])

    for i in range(len(q) // 2):
        q.append(q.popleft())

    if q[0] == q[-1]:
        count = 2
    else:
        count = 1

    for i in range(1, len(q)):
        if q[i] == q[i - 1]:
            count += 1
        else:
            answer.append(count)
            count = 1

    answer.sort()

    return answer