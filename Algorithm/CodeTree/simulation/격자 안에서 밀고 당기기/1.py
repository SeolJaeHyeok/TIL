"""
시계 방향으로 한 칸씩 회전하는 컨베이어 벨트가 있습니다.
컨베이어 벨트 위아래로 n개씩 총 2 * n 개의 숫자가 두 줄로 적혀 있고, 1초에 한 칸씩 움직입니다.

ex) t = 1일 경우
1   2   3       1   1   2
            =>
1   5   6       5   6   3

t초의 시간이 흐른 뒤 컨베이어 벨트에 놓여있는 숫자들의 상태를 출력하는 프로그램을 작성해보세요.
"""
# My
import sys
from collections import deque
input = sys.stdin.readline

n, t = map(int, input().split())
array = deque(map(int, input().split()))
tmp = list(map(int, input().split()))
# 두 개의 배열 합치고
array.extend(tmp)

# t를 배열의 길이로 나눈 나머지만큼 돌리기 => 2 * n번 돌리면 결국 제자리이기 때문
array.rotate(t % (2 * n))

# 출력
array = list(array)
print(*array[:n])
print(*array[n:])

# Sol
# 변수 선언 및 입력
n, t = tuple(map(int, input().split()))
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    # Step 1
    # 위에서 가장 오른쪽에 있는 숫자를 따로 temp값에 저장해놓습니다.
    temp = u[n - 1]

    # Step 2
    # 위에 있는 숫자들을 완성합니다.
    # 오른쪽에서부터 채워넣어야 하며,
    # 맨 왼쪽 숫자는 아래에서 가져와야함에 유의합니다.
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[n - 1]

    # Step 3
    # 아래에 있는 숫자들을 완성합니다.
    # 마찬가지로 오른쪽에서부터 채워넣어야 하며,
    # 맨 왼쪽 숫자는 위에서 미리 저장해놨던 temp값을 가져와야함에 유의합니다.
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp

# 출력
for elem in u:
    print(elem, end=" ")
print()

for elem in d:
    print(elem, end=" ")