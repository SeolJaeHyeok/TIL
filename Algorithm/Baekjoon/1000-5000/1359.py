import sys
from itertools import combinations
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]

choices = list(combinations(arr, m))
answers = list(combinations(arr, m))

count = 0
for answer in answers:
    tmp = 0
    for i in range(len(choices[0])):
        for j in range(len(answer)):
            if choices[0][i] == answer[j]:
                tmp += 1
    if tmp >= k:
        count += 1

print(count / len(choices))