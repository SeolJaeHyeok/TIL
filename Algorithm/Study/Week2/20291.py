# 파일 정리
# 1, 시간 초과
n = int(input())
array = []
tmp = set()
for _ in range(n):
    a, b = input().split('.')
    array.append(b)
    tmp.add(b)

result = []
for i in tmp:
    result.append((i, array.count(i)))

result.sort()
for name, num in result:
    print(name, num)


# 2, 해시 테이블 이용 - 정답
from collections import defaultdict
n = int(input())

data = defaultdict(int)
for _ in range(n):
    a, b = input().split('.')
    data[b] += 1

for k, v in sorted(data.items()):
    print(k, v)

