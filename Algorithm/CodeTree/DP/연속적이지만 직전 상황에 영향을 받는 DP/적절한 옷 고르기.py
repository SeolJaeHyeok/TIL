# 1,
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = [[0] * (n + 1) for _ in range(m + 1)]
s = [0] * (n + 1)
e = [0] * (n + 1)
v = [0] * (n + 1)

# DP 테이블 초기화
for i in range(1, m + 1):
    for j in range(1, n + 1):
        d[i][j] = -sys.maxsize

for i in range(1, n + 1):
    s[i], e[i], v[i] = map(int, input().split())

# 첫 날의 옷을 입는 경우를 초기 조건으로 설정
for j in range(1, n + 1):
    if s[j] == 1:
        d[1][j] = 0

for i in range(2, m + 1):
    for j in range(1, n + 1):
        # i번째 날에 j번의 옷을 입을 수 있는 경우에만 만족도의 최대치를 구할 수 있음
        if s[j] <= i <= e[j]:
            # i - 1번째 날에 k번째 옷을 입을 수 있는 경우를 탐색
            for k in range(1, n + 1):
                # i - 1번째 날에 k번째 옷을 입을 수 있는 경우에만
                # i번째 날에 j번째 옷을 입었을 경우의 만족도 최대치를 갱신할 수 있음
                if s[k] <= i - 1 <= e[k]:
                    d[i][j] = max(d[i][j], d[i - 1][k] + abs(v[j] - v[k]))

print(max(d[-1][:]))

# 2, Sol
import sys
INT_MIN = -sys.maxsize

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
s = [0 for _ in range(n + 1)]
e = [0 for _ in range(n + 1)]
v = [0 for _ in range(n + 1)]

# dp[i][j] :
# i번째 날까지 입을 옷을 전부 결정했고
# 마지막 날에 입은 옷이 j번 옷이라 했을 때,
# 얻을 수 있는 최대 만족도
dp = [
    [0 for _ in range(n + 1)]
    for _ in range(m + 1)
]


def initialize():
    # 최댓값을 구하는 문제이므로,
    # 초기에는 전부 INT_MIN을 넣어줍니다.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = INT_MIN

    # 첫 날에 옷을 입는 경우를 초기 조건으로 설정합니다.
    # 첫 번째 날에 입을 수 있는 옷들에 대해서만 가능하며,
    # j번째 옷을 첫 번째 날에 입는다면
    # 위치 1까지 고려했을 때, 마지막 날에 입은 옷이 j번 옷이 되고,
    # 만족도는 화려함의 차이로 결정되므로 초기 만족도 값은 0 이므로
    # dp[1][j] = 0이 초기 조건이 됩니다.

    for j in range(1, n + 1):
        if s[j] == 1:
            dp[1][j] = 0


for i in range(1, n + 1):
    s[i], e[i], v[i] = tuple(map(int, input().split()))

initialize()

for i in range(2, m + 1):
    # i번째 날까지 입을 옷을 전부 결정했고
    # 마지막 날에 입은 옷이 j번 옷이라 했을 때,
    # 얻을 수 있는 최대 만족도를 계산합니다.

    for j in range(1, n + 1):
        for k in range(1, n + 1):
            # i - 1번째 날에 k번 옷을 입은 경우를 고려해봅니다.
            # 단, k번 옷이 i - 1번째 날에 입을 수 있었어야 하고
            # j번 옷이 i번째 날에 입을 수 있는 경우에만 고려해볼 수 있습니다.
            # 이 상황에서의 최대 만족도를 의미하는 dp[i - 1][k] 값에
            # 새롭게 얻게 되는 만족도는 두 옷의 화려함의 차이이므로
            # |v[j] - v[k]|를 더한 값이 하나의 선택지가 될 수 있습니다.

            if s[k] <= i - 1 and i - 1 <= e[k] and s[j] <= i and i <= e[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(v[j] - v[k]))

# m번째 날짜까지 전부 입을 옷을 결정했을 때,
# 마지막 날에 입은 옷이 j번 옷인 경우 중
# 가장 높은 만족도를 얻을 수 있는 경우를 선택합니다.

ans = max(dp[m][1:n + 1])

print(ans)