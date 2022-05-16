import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
op = list(map(int, input().split()))
arr = deque([i for i in range(1, n + 1)])

count = 0
for o in op:
    idx = arr.index(o)

    if idx > len(arr) // 2:
        arr.rotate(len(arr) - idx)
        count += len(arr) - idx

    elif idx <= len(arr) // 2:
        arr.rotate(-idx)
        count += idx

    del arr[0]


print(count)


