import sys
import math
input = sys.stdin.readline

h, y = map(int, input().split())

d = [0] * (y + 1)
d[0] = h

for i in range(1, y + 1):
    if i < 3: # 3년 미만일 때
        d[i] = math.floor(d[i - 1] * 1.05)
    elif i < 5: # 5년 미만일 때
        d[i] = math.floor(max(d[i - 1] * 1.05, d[i - 3] * 1.2))
    else: # 5년 이상일 때
        d[i] = math.floor(max(d[i - 1] * 1.05, d[i - 3] * 1.2, d[i - 5] * 1.35))

print(d[-1])