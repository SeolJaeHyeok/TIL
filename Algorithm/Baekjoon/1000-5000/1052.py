import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = 0
while bin(n).count('1') > k:
    N = bin(n)[::-1].index('1')
    answer += 2 ** N
    n += 2**N

print(answer)