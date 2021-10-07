# 1026
n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

total = 0
for i in range(n):
    total += A[i] * B[i]

print(total)