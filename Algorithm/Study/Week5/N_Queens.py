# N-Queen
# 1
def n_queens(i, col):
    global count
    # 퀸이 놓인 수
    num = len(col) - 1
    # 상하좌우, 대각선에 다른 퀸이 놓여있지 않은 경우
    if promising(i, col):
        # 퀸이 모든 행에 올바르게 놓인 경우 = n개의 퀸이 모두 체스판에 놓인 경우
        if i == num:
            count += 1
            print(col[1: num+1])
        else:
            # 모든 열에 퀸을 놓아보면서 백트래킹
            for j in range(1, num+1):
                col[i+1] = j
                n_queens(i+1, col)


# 상하좌우, 대각선에 다른 퀸이 위치하는지 확인하는 함수
def promising(i, col):
    k = 1
    while k < i:
        # col[i] == col[k]는 같은 열에 다른 퀸이 위치하는지를 확인
        # abs(col[i] - col[k]) == (i - k)는 왼쪽, 오른쪽 대각선에 다른 퀸이 위치하는지를 확인
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            return False
        k += 1
    return True


n = int(input())
col = [0] * (n + 1)
count = 0
n_queens(0, col)
print(count)


# 2
def dfs(x):
    global count

    if x == N:
        count += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                dfs(x + 1)


def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


N = int(input())
count = 0
row = [0] * N
dfs(0)
print(count)


"""
퀸은 상하좌우, 대각선 방향으로 거리제한없이 이동이 가능하다.
따라서 N-Queen에서 서로 다른 N개의 퀸은 상하좌우, 대각선에 다른 퀸이 존재하면 안된다.
"""