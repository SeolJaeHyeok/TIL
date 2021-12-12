import sys

n = int(input())

# 결과값 - 입력이 한 번씩 진행될 때마다 3개의 줄에 누적, 즉 각 3줄이 n번씩 누적된 값(마지막 줄)이 저장
max_dp = [0] * 3
min_dp = [0] * 3

# 첫 줄은 0을 더한다고 가정하여 초기화
max_val = [0] * 3
min_val = [0] * 3
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    for j in range(3):
        if j == 0:  # 첫 위치일 경우
            # 위쪽과 오른쪽 위 방향에서 접근 가능
            max_val[j] = a + max(max_dp[j], max_dp[j + 1])
            min_val[j] = a + min(min_dp[j], min_dp[j + 1])
        elif j == 1:  # 가운데 위치일 경우
            # 세 방향에서 모두 접근 가능
            max_val[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            min_val[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:  # 마지막 위치일 경우
            # 위쪽과 왼쪽 위 방향에서 접근 가능
            max_val[j] = c + max(max_dp[j], max_dp[j - 1])
            min_val[j] = c + min(min_dp[j], min_dp[j - 1])

    # 세 위치에서 구한 최대값과 최소값을 결과로 저장
    for j in range(3):
        max_dp[j] = max_val[j]
        min_dp[j] = min_val[j]

print(max(max_dp), min(min_dp))


"""
DP는 아직도 잘 모르겠다..
- 점화식을 생각 -> 그에 맞춘 구현
- 그림을 그려서 문제의 규칙을 찾는 연습 필요!! 
"""