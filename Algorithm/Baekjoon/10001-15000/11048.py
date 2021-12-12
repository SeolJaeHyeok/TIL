# 이동하기
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 첫 번째 행과 첫 번째 열의 숫자도 비교하기 위해 1줄 추가
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 왼쪽 위, 위, 왼쪽에서 오는 값들 중 최대값을 더하여 테이블에 추가
        dp[i][j] = array[i - 1][j - 1] + max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])

