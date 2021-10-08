# 2751
# 1, 계수정렬 이용 - 1884ms
import sys

n = int(sys.stdin.readline())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

d = [0] * 2000001
for i in range(len(array)):
    if array[i] < 0:
        d[1000000 - array[i]] += 1
    else:
        d[array[i]] += 1

result = []
for i in range(len(d)):
    if d[i] != 0:
        if i > 1000000:
            result.append(-(i - 1000000))
        else:
            result.append(i)

result.sort()
for i in result:
    print(i)

# 2, 일반적인 정렬 라이브러리 이용 - 1704ms
n = int(sys.stdin.readline())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

for i in array:
    print(i)
