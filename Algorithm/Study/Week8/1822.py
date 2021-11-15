import sys

a, b = map(int, sys.stdin.readline().split())

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

if len(A - B) == 0:
    print(0)
else:
    answer = sorted(A - B)
    print(len(answer))
    for i in answer:
        print(i, end=' ')

