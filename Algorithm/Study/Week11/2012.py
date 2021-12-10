import sys

input = sys.stdin.readline

n = int(input())

array = [0]
for _ in range(n):
    array.append(int(input()))

array.sort()

answer = 0
for i in range(1, n+1):
    answer += abs(array[i] - i)

print(answer)


