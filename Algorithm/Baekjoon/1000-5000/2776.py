import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    num1 = list(map(int, input().split()))
    m = int(input())
    num2 = list(map(int, input().split()))

    table = defaultdict(int)

    for num in num1:
        table[num] += 1

    for num in num2:
        print(1 if table[num] else 0)