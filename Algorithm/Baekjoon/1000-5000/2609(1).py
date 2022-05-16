import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

count = 0
for i in range(n):
    tmp = list(Counter.most_common(array[i]))
    print(tmp)
