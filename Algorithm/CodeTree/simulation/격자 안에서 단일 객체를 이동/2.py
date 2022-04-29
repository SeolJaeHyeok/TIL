"""
0과 1로만 채워져 있는 n * n 크기의 격자판 정보가 주어집니다. 0은 빈 칸을, 1은 해당 칸에 블럭이 채워져 있음을 뜻합니다.
이때 1 * m 크기의 블럭이 격자판 위에서 떨어집니다.
이 블럭은 k번째 열 부터 k + m - 1번째 열까지의 공간을 차지하며, 가장 위에서부터 밑으로 떨어집니다.
만약 이 블럭이 떨어지는 도중 단 한곳에라도 이미 격자판 위에 놓여있던 블럭과 맞닿게 된다거나, 혹은 바닥에 닿게 된다면 떨어지는 것을 멈추게 됩니다.


Input           Output

4 3 1
0 0 0 0         0 0 0 0
0 0 0 1         1 1 1 1
1 0 0 1         1 0 0 1
1 1 1 1         1 1 1 1

4 2 2
0 0 0 0         0 0 0 0
0 0 0 1         0 0 0 1
1 0 0 1         1 1 1 1
1 1 1 1         1 1 1 1

1 1 1
0                  0
"""

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

k -= 1

flag = False # 아래로 진행하면서 범위 내에서 1을 만났을 때를 체크하는 변수
# 첫 번째 행은 항상 0으로 채워져있음이 보장되어 있으므로 두 번째 행부터 반복
for i in range(1, n):
    # 범위 안에 1이 존재할 경우
    if 1 in board[i][k:k + m]:
        # 해당 행 직전의 행의 범위를 1로 채우고
        for j in range(k, k + m):
            board[i - 1][j] = 1
        # 체크한 후 반복문 탈출
        flag = True
        break

    # 1을 만났다면 탈출
    if flag:
        break

# 마지막 행까지 1을 만나지 않은 경우
if not flag:
    # 마지막 행의 해당 범위를 1로 채우기
    for col in range(k, k + m):
        board[-1][col] = 1

for b in board:
    print(*b)