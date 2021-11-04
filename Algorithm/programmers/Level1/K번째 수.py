def solution(array, commands):
    answer = []
    for c in commands:
        start, end, target = c
        tmp = array[start - 1:end]
        tmp.sort()
        answer.append(tmp[target - 1])

    return answer


def solution(array, commands):
    answer = []
    for start, end, target in commands:
        answer.append(sorted(array[start-1:end])[target-1])
    return answer