import sys
input = sys.stdin.readline

n, t = map(int, input().split())
array = [(0, 0)]
for _ in range(n):
    k, s = map(int, input().split())
    array.append((k, s))

# i개 단원을 j시간 동안 공부 했을 때의 최대 점수 테이블
d = [[0 for j in range(t + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, t + 1):
        # array[i][0] = 단원별 예상 공부 시간, array[i][1] = 단원별 예상 점수
        # i번째 단원의 예상 공부 시간이 j 시간보다 작거나 같으면
        if array[i][0] <= j:
            # 현재 단원을 공부했을 경우와 하지 않았을 경우의 예상 점수를 비교 후 갱신
            # d[i - 1][j] = 현재 단원 공부 X
            # d[i - 1][j - array[i][0]] + array[i][1] = 현재 단원 공부 O
            d[i][j] = max(d[i - 1][j], d[i - 1][j - array[i][0]] + array[i][1])
        else:
            d[i][j] = d[i - 1][j]

print(d[n][t])