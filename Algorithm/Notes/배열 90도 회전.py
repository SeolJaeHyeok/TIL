def rotate():
    # next_grid를 0으로 초기화
    for i in range(n):
        for j in range(n):
            tmp_board[i][j] = 0

    # 90' 회전
    for i in range(n):
        for j in range(n):
            tmp_board[i][j] = board[n - j - 1][i]

    # next_grid를 grid에 옮겨주기
    for i in range(n):
        for j in range(n):
            board[i][j] = tmp_board[i][j]

n = 5
board = [list(map(int, input().split())) for _ in range(n)]
tmp_board = [[0 for _ in range(n)] for _ in range(n)]