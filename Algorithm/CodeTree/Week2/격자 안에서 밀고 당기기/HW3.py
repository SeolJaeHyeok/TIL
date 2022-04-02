"""
0과 9 사이의 숫자로만 이루어진 N*M 행렬 모양의 건물에 총 Q번의 바람이 붑니다.
이 바람은 굉장히 특이해서 특정 직사각형 영역의 경계에 있는 숫자들을 시계 방향으로 한 칸씩 shift 하고
해당 직사각형 내 영역에 있는 값들을 각각 자신의 위치를 기준으로 자신과 인접한 원소들과의 평균 값으로 바꿉니다.
(평균 계산시에는 항상 버림하여 정수값이 나오도록 합니다.)

Step1
먼저 직사각형의 경계에 있는 숫자들이 시계 방향으로 한 칸씩 회전을 하게 됩니다.
Step2
그 다음 직사각형 영역 내에 있는 각각의 숫자들의 값이 자신과 인접한 곳에 적혀있는 숫자들과의 평균 값으로 바뀌게 됩니다.
이 과정은 순차적으로 일어나는 것이 아니라 동시에 일어납니다.

한 바람이 분 이후 모든 값 변경이 완료된 이후에 그 다음 바람이 불어 온다고 할 때, 총 Q개의 바람을 거친 이후 건물의 상태를 출력하는 프로그램을 작성해보세요.

Input1
4 6 1
4 5 2 5 6 6
2 6 1 0 5 5
5 1 2 1 6 6
4 2 5 2 8 8
2 2 4 6

Output1
4 5 2 5 6 6
2 3 2 2 3 4
5 3 2 3 4 5
4 3 4 4 7 6

Input2
3 3 2
1 2 3
3 2 1
3 3 3
1 1 2 2
2 2 3 3

Output2
2 2 3
2 2 2
3 2 1
"""

import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
answer = [[0] * (m + 1) for _ in range(n + 1)] # 정답을 저장할 배열
temp_arr = [[0] * (m + 1) for _ in range(n + 1)] # 옮기는 데 사용할 임시 배열


# 경계선에 있는 좌표를 시계 방향으로 한 칸씩 회전시키는 함수
def rotate(start_row, start_col, end_row, end_col):
    # 직사각형 가장 왼쪽 위 모서리 값을 temp에 저장
    temp = answer[start_row][start_col]

    # 직사각형 가장 왼쪽 열을 위로 한 칸씩 이동
    for row in range(start_row, end_row):
        answer[row][start_col] = answer[row + 1][start_col]

    # 직사각형 가장 아래 행을 왼쪽으로 한 칸씩 이동
    for col in range(start_col, end_col):
        answer[end_row][col] = answer[end_row][col + 1]

    # 직사각형 가장 오른쪽 열을 아래로 한 칸씩 이동
    for row in range(end_row, start_row, -1):
        answer[row][end_col] = answer[row - 1][end_col]

    # 직사각형 가장 위 행을 오른쪽으로 한 칸씩 이동
    for col in range(end_col, start_col, -1):
        answer[start_row][col] = answer[start_row][col - 1]

    # 처음에 빼놓은 temp를 가장 왼쪽 위 모서리를 기준으로 바로 오른쪽 칸에 덮어쓰기
    answer[start_row][start_col + 1] = temp


# 해당 좌표와 인접한 네 좌표의 평균을 구하는 함수
def get_average(x, y):
    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]

    sum_value = 0
    mod = 0
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= n and 1 <= ny <= m:
            sum_value += answer[nx][ny]
            mod += 1

    return sum_value // mod


# 평균 값을 구한 배열을 정답 배열에 덮어쓰는 함수
def set_average(start_row, start_col, end_row, end_col):
    # answer와 같은 좌표에 있는 temp_arr의 좌표에 평균 값을 넣고
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            temp_arr[row][col] = get_average(row, col)

    # temp_arr 좌표 값을 answer 좌표에 덮어쓰기
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            answer[row][col] = temp_arr[row][col]


def process(start_row, start_col, end_row, end_col):
    # 직사각형 경계에 있는 숫자들을 시계 방향으로 한 칸씩 회전
    rotate(start_row, start_col, end_row, end_col)
    # 직사각형 내 각각의 숫자들을 인접한 숫자들과의 평균값으로 변경
    set_average(start_row, start_col, end_row, end_col)


# 정답 배열 채우기
for row in range(1, n + 1):
    nums = list(map(int, input().split()))
    for col, num in enumerate(nums, start=1):
        answer[row][col] = num

# 바람 부는 영역 시뮬레이션
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    process(r1, c1, r2, c2)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(answer[i][j], end=' ')
    print()