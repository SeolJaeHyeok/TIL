import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x, y):
    # 범위를 벗어나거나 배추가 심어져 있지 않으면 False 반환
    if x < 0 or x >= m or y < 0 or y >= n or board[y][x] == 0:
        return False

    # 배추가 심어져있다면
    if board[y][x] == 1:
        # 해당 노드 방문처리하고
        board[y][x] = 0
        # 상,하,좌,우 탐색
        bfs(x - 1, y)
        bfs(x + 1, y)
        bfs(x, y - 1)
        bfs(x, y + 1)
        # 탐색 후 True 반환
        return True

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]

    # 배추가 심어진 위치 표시
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1


    count = 0
    # 모든 좌표 탐색
    for i in range(n):
        for j in range(m):
            # 벌레가 이동가능한 최대 범위 탐색 후 True라면 카운팅
            if bfs(j, i):
                count += 1

    print(count)