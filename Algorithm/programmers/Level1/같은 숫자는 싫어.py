def solution(arr):
    answer = []

    prev = 0
    next = 1
    while next < len(arr):
        if arr[prev] != arr[next]:
            answer.append(arr[prev])
        prev, next = next, next + 1

    answer.append(arr[-1])

    return answer

def solution(arr):
    answer = []

    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])

    return answer