import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    print(bin(int(a, 2) + int(b, 2))[2:])