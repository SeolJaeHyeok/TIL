import sys
input = sys.stdin.readline

n = int(input())

# 예외를 깔끔하게 처리하기 위해 0번 인덱스에 0을 넣어줍니다.
a = [0] + list(map(int, input().split()))

# dp[i] : 마지막으로 고른 원소의 위치가 i인
# 부분 수열 중 최장 부분 수열의 길이
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    # i번째 보다 앞에 있는 원소들 중
    # a[i]보다는 값이 작은 곳에
    # 새로운 원소인 a[i]를 추가했을 때의
    # 부분 수열 중 최대 부분 수열의 길이를 계산합니다.
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 마지막 원소의 위치가 i일 때의 부분 수열들 중
# 가장 길이가 긴 부분 수열을 고릅니다.
print(max(dp))