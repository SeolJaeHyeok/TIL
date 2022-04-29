import sys
input = sys.stdin.readline
n = 4
NONE = -1

board = [list(map(int, input().split())) for _ in range(4)]
tmp_board = [[0] * 4 for _ in range(4)]


# 배열을 시계 방향으로 90도 회전시키는 함수
def rotate_board():
    # tmp_board를 0으로 초기화
    for i in range(n):
        for j in range(n):
            tmp_board[i][j] = 0

    # 90도 회전
    for i in range(n):
        for j in range(n):
            tmp_board[i][j] = board[n - j - 1][i]

    # 회전된 값 복사
    for i in range(n):
        for j in range(n):
            board[i][j] = tmp_board[i][j]


# 아래로 숫자들을 떨어뜨리는 함수
def drop():
    # tmp_board를 0으로 초기화합니다.
    for i in range(n):
        for j in range(n):
            tmp_board[i][j] = 0

    # 아래 방향으로 떨어뜨립니다.
    for j in range(n):
        # 같은 숫자끼리 단 한번만
        # 합치기 위해 떨어뜨리기 전에
        # 숫자 하나를 keep해줍니다.
        keep_num, next_row = NONE, n - 1

        for i in range(n - 1, -1, -1):
            if not board[i][j]:
                continue

            # 아직 떨어진 숫자가 없다면, 갱신해줍니다.
            if keep_num == NONE:
                keep_num = board[i][j];

            # 가장 최근에 관찰한 숫자가 현재 숫자와 일치한다면
            # 하나로 합쳐주고, keep 값을 비워줍니다.
            elif keep_num == board[i][j]:
                tmp_board[next_row][j] = keep_num * 2
                keep_num = NONE

                next_row -= 1

            # 가장 최근에 관찰한 숫자와 현재 숫자가 다르다면
            # 최근에 관찰한 숫자를 실제 떨어뜨려주고, keep 값을 갱신해줍니다.
            else:
                tmp_board[next_row][j] = keep_num
                keep_num = board[i][j]

                next_row -= 1

        # 전부 다 진행했는데도 keep 값이 남아있다면
        # 실제로 한번 떨어뜨려줍니다.
        if keep_num != NONE:
            tmp_board[next_row][j] = keep_num
            next_row -= 1
    # tmp_board를 board에 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            board[i][j] = tmp_board[i][j]


# 시뮬레이션
def process():
    # 회전 횟수
    rotate_nums = dir_table[dir]

    # 입력값에 따라 회전시킨 다음
    for i in range(rotate_nums):
        rotate_board()

    # 숫자를 떨어뜨리고
    drop()

    # (n - 회전 횟수)만큼 다시 회전시켜주어 원래 상태로 돌아오게 만들기
    for i in range(n - rotate_nums):
        rotate_board()


# 떨어지는 방향에 따른 회전 횟수
dir = input().rstrip()
dir_table = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}

process()

for i in board:
    print(*i)