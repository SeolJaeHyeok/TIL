import sys
input = sys.stdin.readline

n = int(input())
# 1, 3, 4개의 경우는 무조건 상근이(선)가 이기고 2개의 경우는 무조건 창영(후)이가 이긴다.
d = [0, True, False, True, True] + [0] * (n - 4)

for i in range(5, n + 1):
    # 만약 N - 1, N - 3, N - 4의 경우에서 모두 상근이(선)가 이기는 경우 N번째 돌은 무조건 창영이(후)가 이긴다.
    if d[i - 1] and d[i - 3] and d[i - 4]:
        d[i] = False
        continue
    # 그렇지 않고 하나의 경우라도 상근이가 지는 경우가 생긴다면 N번째 돌은 무조건 상근이가 이긴다.
    d[i] = True

if d[n]:
    print('SK')
else:
    print('CY')