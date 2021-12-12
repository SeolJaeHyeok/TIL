# 배부른 마라토너
# 1, 시간 초과
n = int(input())
candidates = []
for _ in range(n):
    candidates.append(input())

done = []
for _ in range(n - 1):
    done.append(input())

for don in done:
    if don in candidates:
        candidates.remove(don)

print(candidates[0])


# 2, defaultdict 자료형 사용
from collections import defaultdict
import sys

n = int(sys.stdin.readline())
candidates = defaultdict(int)
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    candidates[name] += 1

done = defaultdict(int)
for _ in range(n - 1):
    name = sys.stdin.readline().rstrip()
    done[name] += 1

for key in candidates.keys():
    if key not in done:
        print(key)
        break
    else:
        if candidates[key] != done[key]:
            print(key)
            break




