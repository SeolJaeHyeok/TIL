import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

for i in range(n, 0, -1):
    flag = True
    target = str(i)
    for t in target:
        if int(t) not in array:
            flag = False
            break
    if flag:
        print(i)
        break