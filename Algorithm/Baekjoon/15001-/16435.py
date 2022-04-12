import sys
input = sys.stdin.readline

n, l = map(int, input().split())
heights = list(map(int, input().split()))

heights.sort()

for height in heights:
    if height <= l:
        l += 1
    else: break

print(l)