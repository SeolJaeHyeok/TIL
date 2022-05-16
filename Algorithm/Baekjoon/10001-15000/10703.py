# 1, 시간 초과
import sys
input = sys.stdin.readline

r, s = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

start_row = 0
end_row = 0

# 맨 위 유성의 행
for i in range(r):
    if 'X' in board[i]:
        start_row = i
        break

# 맨 아래 유성의 행
for i in range(r):
    if 'X' not in board[i]:
        end_row = i - 1
        break

# 맨 아래 유성의 열
col_arr = []
for i in range(end_row, end_row + 1):
    for j in range(s):
        if board[i][j] == 'X':
            col_arr.append(j)

# 임시 배열에 원본 배열 복사
a = [[''] * s for _ in range(r)]

for i in range(r):
    for j in range(s):
        if board[i][j] == 'X':
            a[i][j] = '.'
        else:
            a[i][j] = board[i][j]

def move_down(end_row, start_row):
    global a
    # 유성 아래로 한 칸 떨궈서 임시 배열에 저장
    for i in range(end_row, start_row - 1, -1):
        a[i + 1] = board[i]

    # 유성을 떨군 임시 배열을 원본 배열에 붙여넣기
    for i in range(end_row + 1, start_row, -1):
        for j in range(s):
            if board[i][j] == '#':
                continue
            board[i][j] = a[i][j]

    # 떨어진후 가장 높은 위치의 유성보다 높은 위치 모두 공기로 만들기
    for i in range(start_row + 1):
        for j in range(s):
            board[i][j] = '.'


for row in range(end_row + 1, r):
    flag = True
    # 가장 아래의 유성이 아래로 이동 가능한지 확인
    for col in col_arr:
        if board[row][col] == '#':
            flag = False
            break

    # 아래로 이동 가능한 경우
    if flag:
        move_down(end_row, start_row)
        start_row += 1
        end_row += 1
    else:
        break

for i in range(r):
    for j in range(s):
        sys.stdout.write(board[i][j])
    print()

# 2,
import sys
input = sys.stdin.readline

R, S = map(int, input().split())
meteor = [input() for _ in range(R)]  # 유성 충돌 전
arr = [['.'] * S for _ in range(R)]  # 유성 충돌 후

move = 1e9  # 유성이 최종적으로 움직여야하는 거리

for x in range(S):
    temp_meteor = 0  # 가장 높은 유성 행 좌표 (좌표가 높아야 땅과의 거리가 가깝다.)
    temp_ground = 9999  # 가장 낮은 땅 행 좌표 (좌표가 낮아야 유성과의 거리가 가깝다.)
    flag = False
    for y in range(R):
        if meteor[y][x] == 'X':
            temp_meteor = max(temp_meteor, y)
            flag = True  # 유성이 있는 좌표를 만나면 True
        elif meteor[y][x] == '#':
            temp_ground = min(temp_ground, y)
    if flag:  # 유성이 있는 좌표에서 `move` 계산
        move = min(abs(temp_meteor - temp_ground) - 1, move)

for x in range(R):
    for y in range(S):
        if meteor[x][y] == 'X':
            arr[x + move][y] = 'X'  # 유성을 최종 move만큼 움직인다.
        if meteor[x][y] == '#':
            arr[x][y] = '#'

for i in range(R):  # 결과 출력
    for j in range(S):
        sys.stdout.write(arr[i][j])
    sys.stdout.write('\n')