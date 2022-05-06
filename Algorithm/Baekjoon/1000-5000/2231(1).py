import sys
input = sys.stdin.readline

n = int(input())

answer = []
for num in range(1, n + 1):
    tmp_sum = num
    for i in str(num):
        tmp_sum += int(i)

    if tmp_sum == n:
        answer.append(num)

if answer:
    print(min(answer))
else:
    print(0)