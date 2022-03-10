import sys
input = sys.stdin.readline
INF = int(1e9)

# 왼쪽 전구를 기준으로 하는 경
def change_left_light(light, count):
    if count == 1:
        light[-1] = 1 - light[-1]
        light[-2] = 1 - light[-2]

    for i in range(len(light) - 2, -1, -1):
        # 왼쪽 전구가 target과 같은 경우
        if light[i + 1] == target[i + 1]:
            continue
        else:  # 왼쪽 전구가 target과 다른 경우
            count += 1

            # i번째 전구와 i - 1번째 전구를 바꾼 다음
            light[i + 1] = 1 - light[i + 1]
            light[i] = 1 - light[i]
            # 마지막 전구가 아닐 경우 i + 1 번째 전구를 바꿈
            if i > 0:
                light[i - 1] = 1 - light[i - 1]

    if light == target:
        return count

    return INF


def change_right_light(light, count):
    if count == 1:
        light[-1] = 1 - light[-1]
        light[-2] = 1 - light[-2]

    for i in range(len(light) - 2, -1, -1):
        # 오른쪽 전구가 target과 같은 경우
        if light[i + 1] == target[i + 1]:
            continue
        else:  # 오른쪽 전구가 target과 다른 경우
            count += 1

            # i번째 전구와 i + 1번째 전구를 바꾼 다음
            light[i + 1] = 1 - light[i + 1]
            light[i] = 1 - light[i]
            # i번째 전구가 첫 번째 전구가 아닐 경우 i - 1 번째 전구를 바꿈
            if i > 0:
                light[i - 1] = 1 - light[i - 1]

    if light == target:
        return count

    return INF

n = int(input())
array = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

# 왼쪽 전구를 기준으로 하는 경우
case1 = change_left_light(array[:], 1)
case2 = change_left_light(array[:], 0)

if case1 == INF and case2 == INF:
    print(-1)
else:
    print(min(case1, case2))

# 오른쪽 전구를 기준으로 하는 경우
case3 = change_right_light(array[:], 1)
case4 = change_right_light(array[:], 0)

if case3 == INF and case4 == INF:
    print(-1)
else:
    print(min(case3, case4))

