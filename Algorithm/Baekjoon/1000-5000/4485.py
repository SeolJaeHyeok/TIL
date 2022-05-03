import sys
import heapq
input = sys.stdin.readline
INF = 1e9
count = 1

# 다익스트라
def dijkstra():
    q = [] # 비용을 우선하는 우선순위 큐

    # 상하좌우 탐색
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐에 들어가는 정보 = ([x, y]까지 도달하는데 드는 최소 비용, x, y)
    heapq.heappush(q, (board[0][0], 0, 0))
    distance[0][0] = 0
    while q:
        # 현재 위치와 현재 위치까지 도달하는데 드는 비용
        cost, x, y = heapq.heappop(q)

        # 마지막 좌표에 도달했으면 출력
        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않을 경우
            if 0 <= nx < n and 0 <= ny < n:
                # 이동할 좌표까지 드는 비용 = 현재 위치까지의 비용 + 이동할 좌표의 값
                new_cost = cost + board[nx][ny]

                # (nx, ny)까지 이동하는 데에 드는 기존의 비용보다 적게 든다면
                if new_cost < distance[nx][ny]:
                    # (nx, ny)까지 도달하는 최소 비용을 업데이트하고
                    # 새로운 최소 비용과 해당 좌표로 큐에 추가
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

while True:
    n = int(input())

    if n == 0:
        break

    board = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    dijkstra()

    count += 1