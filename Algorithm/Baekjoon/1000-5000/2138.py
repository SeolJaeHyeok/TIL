import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
array = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

def change_light(light, count):
    if count == 1:
        light[0] = 1 - light[0]
        light[1] = 1 - light[1]

    for i in range(1, len(light)):
        # 왼쪽 전구가 target과 같은 경우
        if light[i - 1] == target[i - 1]:
            continue
        else:  # 왼쪽 전구가 target과 다른 경우
            count += 1

            # i번째 전구와 i - 1번째 전구를 바꾼 다음
            light[i - 1] = 1 - light[i - 1]
            light[i] = 1 - light[i]
            # 마지막 전구가 아닐 경우 i + 1 번째 전구를 바꿈
            if i < len(light) - 1:
                light[i + 1] = 1 - light[i + 1]

    if light == target:
        return count

    return INF


case1 = change_light(array[:], 1)
case2 = change_light(array[:], 0)

if case1 == INF and case2 == INF:
    print(-1)
else:
    print(min(case1, case2))
