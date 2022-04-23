import sys
from collections import defaultdict
input = sys.stdin.readline

n, d = map(int, input().split())

table = defaultdict(int)
for i in range(1, n + 1):
    t = str(i)
    for s in t:
        table[s] += 1

print(table[str(d)])