# 1
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = deque(map(int, input().split()))
after = deque(range(1, n + 1))
before = deque([])

while nums:
    o = nums.pop()
    t = after.popleft()

    if o == 1:
        before.appendleft(t)
    elif o == 2:
        before.insert(1, t)
    else:
        before.append(t)

print(*before)

# 2
# 입력 값을 역순으로 바꿔준다.
# 입력값이 1일 때는 덱의 왼쪽에 push를, 2일 때는 덱 왼쪽에서 두번째에 push해주고, 3일 때는 덱의 가장 오른쪽에 push를 해준다.
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
inp = list(map(int, input().split()))
dq = deque([])
inp.reverse()

for i in range(n):
    if inp[i] == 1:
        dq.appendleft(i+1)
    elif inp[i] == 2:
        a = dq.popleft()
        dq.appendleft(i+1)
        dq.appendleft(a)
    elif inp[i] == 3:
        dq.append(i+1)

print(*dq)
