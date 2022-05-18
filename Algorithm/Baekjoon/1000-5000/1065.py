import sys
input = sys.stdin.readline

n = int(input())

answer = 0
for i in range(1, n + 1):
    if i < 100:
        answer += 1
    else:
        num = str(i)
        diff = int(num[0]) - int(num[1])
        for j in range(1, len(num) - 1):
            if int(num[j]) - int(num[j + 1]) == diff:
                answer += 1

print(answer)