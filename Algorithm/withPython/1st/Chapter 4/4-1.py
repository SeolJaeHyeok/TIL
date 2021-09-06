# 상하좌우
# My, 맞히긴 했는데 좀 조잡하다..
n = int(input())
start = [1, 1]
course = list(map(str, input().split()))

for i in range(len(course)):
    if course[i] == 'R':
        if start[1] < n:
            start[1] += 1
    elif course[i] == 'L':
        if start[1] > 1:
            start[1] -= 1
    elif course[i] == 'U':
        if start[0] > 1:
            start[0] += 1
    elif course[i] == 'D':
        if start[0] < n:
            start[0] += 1

print(start)

# sol
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]  # x축이 이동하는 경우는 U, D
dy = [-1, 1, 0, 0]  # y축이 이동하는 경우는 R, L
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
