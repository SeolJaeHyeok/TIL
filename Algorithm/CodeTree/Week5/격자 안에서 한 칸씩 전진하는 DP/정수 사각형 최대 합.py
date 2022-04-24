import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블 초기화
d = [[0] * n for _ in range(n)]
d[0][0] = board[0][0]

# 맨 위쪽 행 계산
for i in range(1, n):
    d[0][i] = d[0][i - 1] + board[0][i]

# 맨 왼쪽 열 계산
for i in range(1, n):
    d[i][0] = d[i - 1][0] + board[i][0]

# 오른쪽과 아래 방향으로 이동이 가능할 때 (i, j)까지 오는 경우는
# 위에서 오는 경우 (i - 1, j) => (i, j)
# 왼쪽에서 오는 경우(i, j - 1) => (i, j)
# 두 경우 중 더 큰 값으로 DP 테이블을 갱신
for i in range(1, n):
    for j in range(1, n):
        # (i, j) 좌표의 값과 왼쪽, 위에서 오는 경우를 합한 값 중 큰 값으로 값 갱신
        d[i][j] = max(board[i][j] + d[i][j - 1], board[i][j] + d[i - 1][j])

print(d[-1][-1])