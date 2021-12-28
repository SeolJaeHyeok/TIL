n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]

# 상하좌우대각선 이동방향 정의
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]

answer = {}
def dfs(x, y, str):
    # 해당 문자열이 등장한 횟수 1 증가시키기
    answer[str] = answer.get(str, 0) + 1
    # 신이 좋아하는 문자열의 길이는 1이상 5이하
    if len(str) == 5:
        return
    # 모든 방향으로 이동
    for i in range(8):
        # 나머지 연산자를 통해 보드의 범위를 벗어날 경우 반대로 이동할 수 있게끔
        nx = (x + dx[i]) % n
        ny = (y + dy[i]) % m

        # 이동할 좌표와 현재 좌표의 문자와 이동할 좌표의 문자열을 더하여 호출
        dfs(nx, ny, str+board[nx][ny])

# 모든 좌표에서 시작
for i in range(n):
    for j in range(m):
        dfs(i, j, board[i][j])

# 신이 좋아하는 문자열의 개수를 출력, 존재하지 않는다면 0
for i in range(k):
    godlike = input()
    print(answer.get(godlike, 0))
