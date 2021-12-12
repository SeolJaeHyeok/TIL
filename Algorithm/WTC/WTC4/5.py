# X
from collections import deque


def solution(rows, columns):
    graph = [[0] * columns for _ in range(rows)]
    visited = [[False] * columns for _ in range(rows)]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        graph[x][y] = 0

        while q:
            x, y = q.popleft()
            # 이동방향(우측, 하단) 정의
            dx = [1, 0]
            dy = [0, 1]
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위를 벗어나면 무시
                if nx < 0 or ny < 0 or nx >= rows or ny >= columns:
                    continue

                if graph[x][y] % 2 == 0:  # 가장 최근의 쓴 숫자가 짝수일 경우
                    if x == rows - 1:  # r = rows
                        graph[0][y] = graph[x][y] + 1
                        q.append((0, y))
                        break
                    graph[x + 1][y] = graph[x][y] + 1
                    q.append((x + 1, y))
                elif graph[x][y] % 2 == 1:  # 가장 최근의 쓴 숫자가 짝수일 경우
                    if y == columns - 1:  # c = columns
                        graph[x][0] = graph[x][y] + 1
                        q.append((x, 0))
                        break

                    graph[x][y + 1] = graph[x][y] + 1
                    q.append((x, y + 1))

    bfs(0, 0)
    # print(graph)
    return graph