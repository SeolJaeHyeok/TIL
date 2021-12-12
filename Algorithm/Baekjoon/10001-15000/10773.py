# 10773
# 1, 시간 초과
k = int(input())

array = []
for i in range(k):
    array.append(int(input()))

tmp = []
for i in range(len(array)):
    if array[i] != 0:
        tmp.append(array[i])
    else:
        tmp = tmp[:-1]

print(sum(tmp))


# 2, sol
import sys

k = int(input())

array = []
for i in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        array.append(num)
    else:
        array = array[:-1]

print(sum(array))