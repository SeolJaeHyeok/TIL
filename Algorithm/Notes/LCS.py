# 1
import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

d = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        # 새로 비교하는 두 문자가 같다면
        if s1[i - 1] == s2[j - 1]:
            # 이전까지의 최대 LCS의 길이에 1을 더해준다
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            # 만약 다르다면 각각의 행과 열에서 이전까지의 최대 LCS의 길이를 비교하여 더 큰 값으로 설정
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[-1][-1])

# 2, Sol
str1 = input()
str2 = input()

str1_len, str2_len = len(str1), len(str2)

# string의 index가 0부터 시작하기 때문에
# 이를 1부터 시작하기 위해서 앞에 #을 추가해줍니다.
str1, str2 = '#' + str1, '#' + str2

dp = [
    [0 for _ in range(str2_len + 1)]
    for _ in range(str1_len + 1)
]


def initialize():
    # dp[1][1] 값은 첫 번째 문자열의 첫 번째 문자와
    # 두 번째 문자열의 첫 번째 문자가 같은지 여부를 저장합니다.
    dp[1][1] = int(str1[1] == str2[1])

    # 두 번째 문자열의 1번 인덱스의 문자까지만 사용했을 때
    # 가능한 부분 수열의 최대 길이를 채워넣어줍니다.
    for i in range(2, str1_len + 1):
        if str1[i] == str2[1]:
            dp[i][1] = 1
        else:
            dp[i][1] = dp[i - 1][1]

    # 첫 번째 문자열의 1번 인덱스의 문자까지만 사용했을 때
    # 가능한 부분 수열의 최대 길이를 채워넣어줍니다.
    for j in range(2, str2_len + 1):
        if str1[1] == str2[j]:
            dp[1][j] = 1
        else:
            dp[1][j] = dp[1][j - 1]


initialize()

for i in range(2, str1_len + 1):
    # 첫 번째 문자열의 i 번째까지 문자열을 고려했고
    # 두 번째 문자열의 j 번째까지 문자열을 고려했을 때
    # 가능한 부분 수열의 최대 길이를 구해줍니다.
    for j in range(2, str2_len + 1):
        # Case 1:
        # 첫 번째 문자열의 i번째 문자와,  두 번째 문자열 j번째 문자가 일치하는 경우
        # 첫 번째 문자열에서 i-1번째 문자까지 고려하고,
        # 두 번째 문자열의 j-1번째 문자까지 고려했을 때
        # 가능한 공통 부분 수열의 뒤에 문자 하나를 새로 추가할 수 있게 됩니다.
        # 따라서 dp[i-1][j-1]에 1을 추가해주면 됩니다
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        # Case 2:
        # 첫 번째 문자열의 i 번째 문자를 공통 부분 수열을 만드는데 고려하지 않는 경우와
        # 두 번째 문자열의 j 번째 문자를 공통 부분 수열을 만드는데 고려하지 않는 경우 중
        # 더 큰 값을 선택하여 줍니다.
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[str1_len][str2_len])