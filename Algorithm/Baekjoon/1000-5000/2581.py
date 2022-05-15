import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

answer = []
for i in range(n, m + 1):
    if i == 1:
        continue
    if check(i):
        answer.append(i)

if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)
