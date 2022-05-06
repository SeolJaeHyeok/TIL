import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

answer_x = 0
answer_y = 0
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (b * d - a * e) * y == c * d - a * f and (a * e - b * d) * x == c * e - b * f:
            answer_x = x
            answer_y = y


print(answer_x, answer_y)