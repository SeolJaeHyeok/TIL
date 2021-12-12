# 종이 자르기
x, y = map(int, input().split())
n = int(input())
width = [0, x]
height = [0, y]

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        height.append(b)
    elif a == 1:
        width.append(b)

width.sort()
height.sort()

maxResult = 0
for i in range(1, len(width)):
    w = width[i] - width[i - 1]
    for j in range(1, len(height)):
        h = height[j] - height[j - 1]
        maxResult = max(maxResult, w*h)

print(maxResult)
