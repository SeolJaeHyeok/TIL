import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n + 1)
if n <= 3:
    print(1)
else:
    d[1] = d[2] = d[3] = 1
    for i in range(4, n + 1):
        d[i] = d[i-1] + d[i - 3]

    print(d[n])
