"""
좌표평면 위 (0, 0)에서 북쪽을 향한 상태에서 움직이는 것을 시작하려 합니다.
N개의 명령에 따라 총 N번 움직이며,
명령 L이 주어지면 왼쪽으로 90도 방향 전환을,
명령 R이 주어지면 오른쪽으로 90도 방향전환을 하고,
명령 F가 주어지면 바라보고 있는 방향으로 한칸 이동하려고 합니다.
1초에 한 칸씩 움직이며, 회전에도 1초의 시간이 걸린다 했을 때, 몇 초 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지를 판단하는 프로그램을 작성해보세요.

Input
FFFRFFRFFFRFFFFFF

Ouput
13
"""
import sys
input = sys.stdin.readline

words = input()

x, y, dir = 0, 0, 3 # 초기 위치 및 이동 방향
# 동, 남, 서, 북
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

flag = False
time = 0

for word in words:
    if word == 'F':  # 직진
        # 앞으로 한 칸 이동
        x = x + dx[dir]
        y = y + dy[dir]
    elif word == 'R':  # 시계방향 90도 회전
        dir = (dir + 1) % 4
    else:  # 반시계방향 90도 회전
        dir = (dir - 1 + 4) % 4

    # 이동 및 회전에 따른 시간 증가
    time += 1

    # 초기 위치(0, 0)으로 돌아왔을 경우 걸린 시간 출력
    if x == 0 and y == 0:
        print(time)
        flag = True
        break

# 초기 위치에 도달하지 못했을 경우 -1 출력
if not flag:
    print(-1)