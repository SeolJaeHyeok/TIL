# BFS
import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

answer = -1
q = deque()
q.append((a, 1))
# A -> B
while q:
    num, cnt = q.popleft()

    if num == b:
        answer = cnt
        break

    # a x 2가 b보다 작으면 큐에 추가
    if num * 2 <= b:
        q.append((num * 2, cnt + 1))

    # a + '1'이 b보다 작아도 큐에 추가
    if int(str(num) + '1') <= b:
        q.append((int(str(num) + '1'), cnt + 1))

print(answer)

# Greedy
import sys

A, B = map(int, sys.stdin.readline().split())

count = 1
# B -> A
while True:
    # 같으면 탈출
    if A == B:
        break
    if A > B or (B % 10 != 1 and B % 2 != 0): # A가 B보다 커지거나 두 연산이 모두 불가능한 경우 탈출
        count = -1
        break

    if B % 10 == 1: # 1을 빼는 것이 더 효율적인 연산이 되므로 10으로 나눴을 때 1이 남으면 1을 뺴준다.
        B //= 10
        count += 1
    elif B % 2 == 0: # 위 조건에 부합하지 않으면 2로 나누기
        B //= 2
        count += 1

print(count)

