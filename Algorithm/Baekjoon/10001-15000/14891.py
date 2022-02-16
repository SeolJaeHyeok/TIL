import sys
from collections import deque
input = sys.stdin.readline


# 톱니 회전시키는 함수
def rotate(n, d):
    return array[n].rotate(d)


# 오른쪽 톱니 회전 여부 체크
def check_right(start, dir):
    # 범위를 벗어나거나 양 극이 같을 경우 탈출
    if start > 4 or array[start - 1][2] == array[start][6]:
        return

    # 양 극이 다를 경우 재조사
    if array[start - 1][2] != array[start][6]:
        check_right(start + 1, -dir)
        # 조사가 끝난 후 톱니 회전
        rotate(start, dir)


# 왼쪽 톱니 회전 여부 체크
def check_left(start, dir):
    # 범위를 벗어나거나 양 극이 같을 경우 탈출
    if start < 1 or array[start][2] == array[start + 1][6]:
        return
    # 양 극이 다를 경우 재조사
    if array[start][2] != array[start + 1][6]:
        check_left(start - 1, -dir)
        # 조사가 끝난 후 톱니 회전
        rotate(start, dir)


array = {}
for i in range(1, 5):
    array[i] = deque(map(int, input().rstrip()))

k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())

    # 양 극이 다를 경우 서로 반대 방향으로 회전하기 때문에 -dir
    check_right(num + 1, -dir) # 오른쪽 조사
    check_left(num - 1, -dir) # 왼쪽 조사

    rotate(num, dir) # 조사가 끝난 뒤 톱니 회전

# 조건에 맞춰 출력
answer = 0
for i in range(1, 5):
    if array[i][0] == 1:
        answer += 2 ** (i - 1)

print(answer)


