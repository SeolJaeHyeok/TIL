"""
방향 회전을 위한 dx, dy 정의 방법
"""
import sys
input = sys.stdin.readline

orders = input()
x, y = 0, 0

# 동, 남, 서, 북
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir = 3
for order in orders:
    if order == 'L':
        # 왼쪽으로 회전
        dir = (dir - 1 + 4) % 4
    elif order == 'R':
        # 오른쪽으로 회전
        dir = (dir + 1) % 4
    else:
        # 앞으로 이동
        x, y = x + dx[dir], y + dy[dir]
print(x, y)