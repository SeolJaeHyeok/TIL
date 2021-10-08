# 10250
t = int(input())

for i in range(t):
    H, W, N = map(int, input().split())
    roomNum = N // H + 1
    floor = N % H
    if N % H == 0:
        roomNum = N // H
        floor = H
    answer = floor*100 + roomNum
    print(answer)

