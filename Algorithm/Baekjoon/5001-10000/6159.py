import sys
input = sys.stdin.readline

n, s = map(int, input().split())
cows = [int(input()) for _ in range(n)]

cows.sort()
answer = 0

for i in range(len(cows)):
    for j in range(i + 1, len(cows)):
        if cows[i] + cows[j] <= s:
            answer += 1
        else:
            break

print(answer)