# 빙글빙글 스네일
# 1
n = int(input())
d, cnt, i, x, y, k = [0] * 6
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while cnt < n and i < n:
    if cnt % 2 == 0:
        k += 1
    for j in range(k):
        print(x, y)
        x += dx[d]
        y += dy[d]
        i += 1
        if i >= n:
            break
    d = (d + 1) % 4
    cnt += 1
print(x, y)

# 2
# 이동거리는 1,1,2,2,3,3,4,4,5,5,6,6....
n = int(input())

y = x = 0
dirs = [0, 1, 0, -1, 0]
d = 0
stack = [1, 0]  # 이동거리,현재 이동거리로 이동한 횟수

while n:

    x += dirs[d]
    y += dirs[d + 1]

    stack[1] += 1

    if stack[1] == stack[0]:
        d = (d + 1) % 4

    if stack[1] == stack[0] * 2:
        d = (d + 1) % 4
        stack[0] += 1
        stack[1] = 0

    n -= 1

print(x, y)