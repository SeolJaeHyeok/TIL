n = int(input())
array = [input() for _ in range(n)]

# 심장
x = y = 0
for i in range(n):
    for j in range(n):
        if array[i][j] == '*':
            x, y = i+2, j+1
            print(x, y)
            break
    if x and y:
        break

# 왼팔
left_arm = 0
for i in range(y-1):
    if array[x-1][i] == '*':
        left_arm += 1

# 오른팔
right_arm = 0
for i in range(y, n):
    if array[x-1][i] == '*':
        right_arm += 1

# 허리
center = 0
for i in range(x, n):
    if array[i][y-1] == "*":
        center += 1

# 왼쪽 다리
left_leg = 0
for i in range(x+center, n):
    if array[i][y-2] == '*':
        left_leg += 1

# 오른쪽 다리
right_leg = 0
for i in range(x+center, n):
    if array[i][y] == '*':
        right_leg += 1

print(left_arm, right_arm, center, left_leg, right_leg)


