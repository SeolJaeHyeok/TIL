# 성 지키기
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(input())

row_count = col_count = 0

for i in range(n):
    # 행(가로)을 기준으로 탐색
    if 'X' not in array[i]:
        row_count += 1

for j in range(m):
    # 열(세로)을 기준으로 탐색
    if 'X' not in [array[i][j] for i in range(n)]:
        col_count += 1

# 둘 중 큰 값이 최소 경비원의 수
print(max(row_count, col_count))

