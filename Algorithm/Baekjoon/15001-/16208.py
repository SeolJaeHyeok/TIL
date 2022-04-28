import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
total = sum(arr)

answer = 0
for a in arr:
    answer += (a * (total - a))
    total -= a

print(answer)