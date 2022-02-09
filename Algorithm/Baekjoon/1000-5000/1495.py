import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))

d = [[False] * (m + 1) for _ in range(n + 1)] # 연주 가능한 모든 경우의 수 초기화
d[0][s] = True # 시작 볼륨 체크

for i in range(n):
    for j in range(m + 1):
        check = d[i][j]
        # 연주가 가능할 경우
        if check:
            # 볼륨을 늘리거나 줄였을 때 연주가 가능한지 체크
            if j + volumes[i] <= m:
                d[i + 1][j + volumes[i]] = True
            if j - volumes[i] >= 0:
                d[i + 1][j - volumes[i]] = True

# 마지막 곡에서 최대 볼륨 추출
answer = -1
for i in range(m + 1):
    if d[n][i]:
        answer = i

print(answer)
"""
모든 경우에 대하여 연주가 가능한지 여부를 체크한 후 -> (n) * (m + 1)개의 경우
마지막 곡의 연주가 가능할 경우 최대 볼륨을 추출
"""