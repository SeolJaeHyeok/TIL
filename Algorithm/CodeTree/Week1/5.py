"""
달팽이 배열
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = [[0] * m for _ in range(n)]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


x, y = 0, 0  # 초기 좌표
# 이동 방향 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer[x][y] = 1  # 초기 좌표 값
dir = 0  # 초기 이동 방향

for i in range(2, n * m + 1):
    # 현재 좌표와 방향을 기준으로 이동할 좌표
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 이동할 좌표가 범위를 벗어나거나 이미 접근한 적이 있는 좌표라면 방향 바꾸기(90도 회전)
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir = (dir + 1) % 4

    # 좌표 값 바꿔주고
    x, y = x + dx[dir], y + dy[dir]
    # 바꾼 좌표 값에 값 추가
    answer[x][y] = i

for i in answer:
    print(*i)