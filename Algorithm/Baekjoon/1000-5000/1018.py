import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

answer = []
count = 0
for i in range(n - 7):
    for j in range(m - 7):
        w = b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        w += 1
                    elif board[k][l] != 'B':
                        b += 1
                else:
                    if board[k][l] != 'W':
                        b += 1
                    elif board[k][l] != 'B':
                        w += 1
        answer.append(w)
        answer.append(b)

print(min(answer))
