import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(n)]
B = [list(map(int, input().rstrip())) for _ in range(n)]

# 3x3 크기만큼의 부분 행렬을 뒤집는 함수
def process(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            A[i][j] = 1 - A[i][j]

count = 0
# NxM 크기의 행렬에서 3x3 크기의 부분행렬로 연산이 가능한 횟수는 (0, 0) ~ (n-3, m-3)
for i in range(n - 2):
    for j in range(m - 2):
        # A, B 행렬의 값이 같지 않을 경우 뒤집기 연산 수행
        if A[i][j] != B[i][j]:
            process(i, j)
            count += 1

if A == B:
    print(count)
else:
    print(-1)