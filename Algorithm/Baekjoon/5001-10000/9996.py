import sys

N = int(sys.stdin.readline())
pt = sys.stdin.readline().rstrip().split("*")
front = len(pt[0])
back = len(pt[1])

for i in range(N):
    st = sys.stdin.readline().rstrip()
    st_front = st[:front]
    st = st[front:]
    st_back = st[len(st) - back:]

    if len(st) == 1:
        print("NE")
    elif st_front == pt[0] and st_back == pt[1]:
        print("DA")
    else:
        print("NE")