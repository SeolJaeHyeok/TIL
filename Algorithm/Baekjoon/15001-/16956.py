import sys
input = sys.stdin.readline

r, c = map(int, input().split())

board = []
for i in range(r):
    board.append(list(input().rstrip()))

flag = False
for x in range(r):
    for y in range(c):
        # 늑대인 경우
        if board[x][y] == 'W':
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            # 상하좌우 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위를 벗어나면 무시
                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    continue
                # 늑대의 상하좌우에 양이 있다면 체크
                if board[nx][ny] == 'S':
                    flag = True
                    break
        # 양인 경우 무시
        elif board[x][y] == 'S':
            continue
        # 비어있는 경우 울타리로 채움
        else:
            board[x][y] = 'D'

if flag:
    print(0)
else:
    print(1)
    for i in board:
        print(''.join(i))
