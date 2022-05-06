import sys
from itertools import permutations
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

per = list(permutations(array, n))

count = 0
for pe in per:
    weight = 500
    flag = True
    for p in pe:
        weight += (p - k)
        if weight < 500:
            flag = False
            break
    if flag:
        count += 1
print(count)