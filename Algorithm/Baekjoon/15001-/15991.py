import sys
input = sys.stdin.readline

t = int(input())

d = [0] * 100001
d[1], d[2], d[3], d[4], d[5], d[6] = 1, 2, 2, 3, 3, 6

for i in range(7, 100001):
    d[i] = (d[i - 2] + d[i - 4] + d[i - 6]) % 1000000009

for _ in range(t):
    n = int(input())
    print(d[n])