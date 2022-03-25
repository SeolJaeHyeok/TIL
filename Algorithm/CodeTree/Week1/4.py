import sys

input = sys.stdin.readline

n, t = map(int, input().split())
r, c, d = map(str, input().split())

# 이동 방향 및 바라보는 방향 초기화
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
dir_dict = {'R': 0, 'D': 1, 'U': 2, 'L': 3}


def move(x, y, d):
    # 이동 방향 설정
    dir = dir_dict[d]

    # t초만큼 반복
    for i in range(t):
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 이동한 좌표가 범위 안에 있다면 값 갱신
        if 0 <= nx < n and 0 <= ny < n:
            x, y = nx, ny
        else:  # 범위를 벗어난다면 방향 전환
            dir = 3 - dir

    print(x + 1, y + 1)


move(int(r) - 1, int(c) - 1, d)