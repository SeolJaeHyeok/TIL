from collections import deque

# board의 변화를 보기 위한 함수
def printBoard(arr, r, c):
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end=' ')
        print()

def bfs():
    q = deque()
    q.append([0, 0]) # (0, 0)부터 시작
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if board[nx][ny] == 0 and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                # 처음으로 1을 만나면 추가해주는 것이 아닌 0으로 만들어 주고(녹인 다음) 녹인 치즈의 개수 카운팅
                elif board[nx][ny] == 1:
                    board[nx][ny] = 0
                    count += 1
                    visited[nx][ny] = True
    return count


row, col = map(int, input().split())

board = []
for _ in range(row):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
time = 0
while True:
    visited = [[False] * col for _ in range(row)] # 방문 처리를 계속 가지고 가야되므로 안에서 선언
    cnt = bfs() # 녹인 치즈의 개수를 구하고
    result.append(cnt)
    # 녹인 치즈의 개수가 0개가 되면 탈출
    if cnt == 0:
        break
    time += 1
    printBoard(board, row, col)
    print()

# 걸린 시간과 한 시간 전의 치즈 개수 출력
print(time)
print(result[-2])


