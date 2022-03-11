# sol
def solution(arr):
    minmax = [0, 0]
    value = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == '+':
            continue
        elif arr[i] == '-':
            tempmin, tempmax = minmax
            minmax[0] = min(-(value + tempmax), -value + tempmin)

            minus_v = int(arr[i + 1])
            minmax[1] = max(-(value + tempmin), -minus_v + (value - minus_v) + tempmax)

            value = 0
        elif int(arr[i]) >= 0:
            value += int(arr[i])
    minmax[1] += value

    return minmax[1]


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))