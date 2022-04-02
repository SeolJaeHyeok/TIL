"""
n * m크기의 이차원 영역의 각 위치에 정수 값이 하나씩 적혀있습니다.
이 영역 안에서 가능한 양수 직사각형 중 최대 크기를 구하려고 합니다.
양수 직사각형이란, 직사각형의 변들이 주어진 격자 판에 평행하면서, 직사각형 내에 있는 숫자들이 전부 양수인 직사각형을 의미합니다.
최대 크기의 양수 직사각형을 찾는 프로그램을 작성해보세요.

Input           Output
3 3
1 2 3
3 4 5             9
6 7 8

4 5
6 -2 4 -3 1
3 6 7 -4 1        6
6 1 8 15 -5
3 -5 1 16 3
"""
# My, 7%
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# (row, col) ~ (row_e, col_e)까지의 면적을 구하는 함수
def get_area(row, col, row_e, col_e):
    area = 0
    for r in range(row, row_e + 1):
        for c in range(col, col_e + 1):
            # 범위를 벗어나면 종료
            if r >= n or c >= m:
                return
            # 해당 범위 내의 음수가 포함되어 있으면 종료
            if board[r][c] < 0:
                return -1
            area += 1
    return area

answer = -1
for i in range(n):
    for j in range(m):
        for k in range(n):
            for l in range(m):
                result = get_area(i, j, k, l)
                answer = max(answer, result)

print(answer)