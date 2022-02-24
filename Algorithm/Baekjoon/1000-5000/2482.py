import sys
input = sys.stdin.readline

n = int(input())
k = int(input())


d = [[0] * (k + 1) for _ in range(n + 1)]

# 선형으로 이어진 모든 경우의 수를 구한 다음
# 선형일 때의 점화식 => n가지 색상 중 k개를 선택하는 경우 = n-2가지 색상까지 k-1개를 선택하는 경우 + n-1가지 색상까지 k개를 선택하는 경우
# d[n][k] = d[n - 2][k - 1] + d[n - 1][k]
for i in range(n + 1):
    d[i][0] = 1
    d[i][1] = i
# 서로 다른 2개 이상의 색상을 선택할 수 있는 방법
for i in range(2, n + 1):
    for j in range(1, k + 1):
        d[i][j] = (d[i - 2][j - 1] + d[i - 1][j]) % 1000000003

# 1번째와 N번째가 붙어있는 원형을 띄고 있으므로 원형일 떄의 경우의 수를 구하는 점화식을 적용
# 원형일 때의 점화식 => n가지 색상까지 k개를 선택하는 경우 = n-3가지 색상까지 k-1개를 선택하는 경우 + n-1가지 색상까지 k개를 선택하는 경우
# d[n][k] = d[n - 3][k - 1] + d[n - 1][k]
answer = (d[n - 3][k - 1] + d[n - 1][k]) % 1000000003
print(answer)