n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 맵 정보 입력받기
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 방문처리를 위한 맵 초기화
visited = [[0] * m for _ in range(n)]
# 현재 위치 방문 처리
visited[x][y] = 1

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if not visited[nx][ny] and board[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 청소할 공간이 없는 경우
    else:
        # 회전만 하고 돌아감
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤 쪽으로 이동할 수 있는 경우 이동
        if board[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤 쪽 방향이 벽이라 이동할 수 없는 경우 탈출
        else:
            break
        turn_time = 0

print(count)

