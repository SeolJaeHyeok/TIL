import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
for i in range(n):
    for j in range(n):
        x, y = i, j # 시작 좌표
        tmp_count = 0
        # 상, 하, 좌, 우 이동
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위를 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 1이면 카운팅
            if board[nx][ny] == 1:
                tmp_count += 1
        # 해당 좌표의 상,하,좌,우 좌표 중 1의 개수가 3이상이면 카운팅
        if tmp_count >= 3:
            answer += 1

print(answer)