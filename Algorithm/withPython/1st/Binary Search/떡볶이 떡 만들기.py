import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start = 0
end = array[-1]
while start <= end:
    mid = (start + end) // 2
    tot = 0
    for i in array:
        if i > mid:
           tot += (i - mid)

    if tot == m:
        print(mid)
        break
    elif tot > m:
        start = mid + 1
    else:
        end = mid - 1

# 4 6
# 19 15 10 17