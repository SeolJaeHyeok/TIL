import sys
input = sys.stdin.readline

"""
명령에 따른 주사위 값의 주사위 값의 변화
 동       서       남       북
1->3    1->4    1->5    1->2
2->2    2->2    2->1    2->6
3->6    3->1    3->3    3->3
4->1    4->6    4->4    4->4
5->5    5->5    5->6    5->1
6->4    6->3    6->2    6->5
"""
# 위의 규칙에 따라 주사위 값을 변화시킬 함수
def move_dice(order, dice):
    if order == 1: # 동
        return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif order == 2: # 서
        return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif order == 3: # 북
        return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif order == 4: # 남
        return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0] * 6 # 초기 주사위 설정
for i in range(len(orders)):
    # 명령에 따라 이동할 좌표 설정
    dir = orders[i] - 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 이동한 좌표가 지도의 범위를 벗어나면 무시
    if nx >= n or ny >= m or nx < 0 or ny < 0:
        continue

    # 주사위 이동
    dice = move_dice(orders[i], dice)

    # 이동한 칸의 값이 0이 아니면
    if board[nx][ny] != 0:
        # 이동한 칸의 값이 주사위 바닥면으로 복사
        dice[5] = board[nx][ny]
        # 칸의 값은 0으로 변경
        board[nx][ny] = 0
    else: # 이동한 칸의 값이 0이라면
        # 주사위의 바닥면이 지도의 칸에 복사
        board[nx][ny] = dice[5]

    # x, y 값 갱신
    x, y = nx, ny
    # 주사위의 윗면 출력
    print(dice[0])
