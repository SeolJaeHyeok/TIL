# 터렛
import math

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 중심 사이의 거리

    if distance == 0 and r1 == r2:  # 원의 중심이 같고 반지름의 길이도 같을 경우
        print(-1)
    elif r1 + r2 == distance or abs(r1-r2) == distance:  # 내,외접일 경우
        print(1)
    elif abs(r1-r2) < distance < r1 + r2:  # 두 점에서 만났을 경우
        print(2)
    else:  # 두 점이 떨어져 있을 경우
        print(0)