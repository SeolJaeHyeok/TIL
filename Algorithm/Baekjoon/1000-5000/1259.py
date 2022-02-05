import sys
input = sys.stdin.readline

while True:
    n = int(input())
    tmp = str(n)
    if n == 0:
        sys.exit()
    if tmp == tmp[::-1]:
        print('yes')
    else:
        print('no')