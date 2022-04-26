import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def append_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN//3)
    # print(Stars)
    L = []

    # 첫 번째 줄
    for S in Stars:
        L.append(S*3)
    # 두 번째 줄
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    # 세 번째 줄
    for S in Stars:
        L.append(S*3)

    return L


n = int(input())
for i in append_star(n):
    print(i)

