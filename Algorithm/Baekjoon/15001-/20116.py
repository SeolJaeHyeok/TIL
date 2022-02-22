import sys
input = sys.stdin.readline

n, L = map(int, input().split())
w = list(map(int, input().split()))

d = [0] * n
d[n - 1] = w[n - 1]
for i in range(n - 2, 0, -1):
    d[i] = w[i] + d[i + 1]

mod = 1
for i in range(len(w) - 1, 0, -1):
    s, e = w[i - 1] - L, w[i - 1] + L
    target = d[i] / mod
    if s < target < e:
        mod += 1
        continue
    else:
        print('unstable')
        sys.exit()

print('stable')