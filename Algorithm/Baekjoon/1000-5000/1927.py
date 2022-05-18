import sys
import heapq
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    num = int(input())
    if num == 0 and not arr:
        print(0)
        continue
    if num > 0:
        heapq.heappush(arr, num)
    if num == 0:
        print(heapq.heappop(arr))