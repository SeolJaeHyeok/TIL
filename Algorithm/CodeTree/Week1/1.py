"""
방향에 맞춰 이동
"""
# 1
import sys
input = sys.stdin.readline

n = int(input())
orders = []
for i in range(n):
    c, n = map(str, input().split())
    orders.append((c, n))

# 남, 서, 북, 동
dx = [0, -1, 0 ,1]
dy = [1, 0, -1, 0]

x, y = 0, 0
for c, n in orders:
    if c == 'N':
        y += int(n)
    elif c == 'E':
        x += int(n)
    elif c == 'W':
        x -= int(n)
    else:
        y -= int(n)

print(x, y)

# 2
import sys

input = sys.stdin.readline

n = int(input())

# 남, 서, 북, 동
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
x, y = 0, 0
dir = -1
for i in range(n):
    c, n = map(str, input().split())
    n = int(n)
    if c == 'N':
        dir = 2
    elif c == 'E':
        dir = 3
    elif c == 'W':
        dir = 1
    else:
        dir = 0

    x, y = x + dx[dir] * n, y + dy[dir] * n

print(x, y)