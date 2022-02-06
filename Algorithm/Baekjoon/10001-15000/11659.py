import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
d = [0] * len(array)


for i in range(len(array)):
    if i == 0:
        d[i] = array[i]
    else:
        d[i] = array[i] + d[i - 1]

for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        print(d[b-1])
    else:
        print(d[b-1] - d[a-2])
