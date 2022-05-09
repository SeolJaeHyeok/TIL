# 1,
# 현재를 기준으로 얻을 수 있는 수익과
# 오늘 이전까지 발생한 수익들 중 현재 발생 가능한 수익에 더할 수 있는 수익(이전 상담이 이미 끝난 상태의 수익)의 모든 경우를 검사하여 최댓값 갱신
# 시간 초과
import sys
input = sys.stdin.readline

n = int(input())
table = [[0, 0]]
for _ in range(n):
    t, p = map(int, input().split())
    table.append([t, p])

d = [0] * (n + 1)
d[1] = table[1][1]

# 1000 * 1500000
for i in range(2, n + 1):
    if i + table[i][0] <= n + 1:
        for j in range(i - 1, 0, -1):
            if j + table[j][0] <= i:
                d[i] = max(d[i], table[i][1] + d[j])

print(max(d))

# 현재 업무가 끝나 수익이 발생하는 날의 값을 갱신시켜주는 방식
import sys
input = sys.stdin.readline

n = int(input())
table = []

for _ in range(n):
    t, p = map(int, input().split())
    table.append([t, p])

d = [0] * (n + 1)

M = 0
for i in range(n):
    M = max(M, d[i])
    if i + table[i][0] > n:
        continue
    d[i+table[i][0]] = max(M+table[i][1], d[i+table[i][0]])

print(max(d))