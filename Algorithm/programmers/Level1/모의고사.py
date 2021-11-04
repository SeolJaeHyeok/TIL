from collections import deque

def solution(answers):
    a = deque([1, 2, 3, 4, 5])
    b = deque([2, 1, 2, 3, 2, 4, 2, 5])
    c = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    score = [[1, 0], [2, 0], [3, 0]]
    for answer in answers:
        if a[0] == answer:
            score[0][1] += 1
        if b[0] == answer:
            score[1][1] += 1
        if c[0] == answer:
            score[2][1] += 1

        a.append(a.popleft())
        b.append(b.popleft())
        c.append(c.popleft())

    score.sort(key=lambda x: x[1], reverse=True)

    answer = []
    max_score = score[0][1]
    answer.append(score[0][0])
    for i in range(1, len(score)):
        if score[i][1] == max_score:
            answer.append(score[i][0])
        else:
            break

    return answer


def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    for i, answer in enumerate(answers):
        if a[i % len(a)] == answer:
            score[0] += 1
        if b[i % len(b)] == answer:
            score[1] += 1
        if c[i % len(c)] == answer:
            score[2] += 1

    answer = []
    max_score = max(score)
    for i in range(len(score)):
        if score[i] == max_score:
            answer.append(i + 1)

    return answer