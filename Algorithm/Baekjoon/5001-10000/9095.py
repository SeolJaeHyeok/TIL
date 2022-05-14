# 1, itertools 이용
import sys
from itertools import product
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    arr = [1, 2, 3]
    for i in range(1, n + 1):
        for pro in list(product(arr, repeat=i)):
            if sum(pro) == n:
                count += 1

    print(count)

# 2, Backtracking
import sys
input = sys.stdin.readline

def Choose(sum_value):
    global count

    if sum_value > n:
        return

    if sum_value == n:
        count += 1
        return

    for i in range(1, 4):
        answer.append(i)
        Choose(sum_value + i)
        answer.pop()

    return

t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    count = 0
    Choose(0)
    print(count)
