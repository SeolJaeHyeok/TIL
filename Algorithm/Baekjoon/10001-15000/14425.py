# 문자열 집합
import sys
from collections import defaultdict
n, m = map(int, sys.stdin.readline().split())

array = defaultdict(int)
for _ in range(n):
    data = sys.stdin.readline().rstrip()
    array[data] += 1

search = []
for _ in range(m):
    search.append(sys.stdin.readline().rstrip())

count = 0
for i in range(len(search)):
    if array[search[i]]:
        count += 1
    else:
        continue
print(count)
