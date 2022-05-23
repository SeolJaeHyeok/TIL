import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(2)]
visited = [[False] * n for _ in range(n)]

def bfs(i, j):
    dead = 0
    q = deque()
    q.append((i, j))
    while q:
        for _ in range(len(q)):
            # 현재 줄과 현재 위치한 칸
            x, y = q.popleft()

            # 세가지 행동에 대해서 검사
            for next_x, next_y in ((x, y + 1), (x, y - 1), (~x, y + 3)):
                # 탈출이 가능한 경우
                if next_y >= n:
                    return 1

                # 이동하는 칸이 1이면서 방문하지 않았고 범위 내에 있으면 방문 처리하고 큐에 추가
                if board[next_x][next_y] and not visited[next_x][next_y] and 0 < next_y < n:
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True

        dead += 1

    return 0

print(bfs(0, 0))
