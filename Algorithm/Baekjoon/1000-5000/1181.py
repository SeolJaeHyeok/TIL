import sys
input = sys.stdin.readline

n = int(input())
array = set()
for _ in range(n):
    array.add(input().rstrip())

array = list(array)
array.sort(key=lambda x: (len(x), x))

for i in array:
    print(i)
